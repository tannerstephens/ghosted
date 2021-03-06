from flask import render_template, Blueprint, session, url_for, request, flash, redirect, send_file
import random
import json

from ..ghost_pdf_generator import generate
from ..extensions import db
from ..models import Spectre, Haunt

views = Blueprint('views', __name__)

@views.before_request
def make_session_perm():
  session.permanent = True

def generate_gids(n):
  ids = []

  while len(ids) < n:
    new_id = ''.join([chr(random.randint(65,90)) for _ in range(8)])

    if Spectre.query.filter_by(ghost_id=new_id).first() == None:
      ids.append(new_id)

  return tuple(ids)

@views.route('/')
def home():
  ghost_id = session.get('id')

  if not ghost_id:
    return render_template('pages/home.html')

  return redirect(url_for('views.haunt'))

@views.route('/new')
def new_haunt():
  haunt = Haunt()
  db.session.add(haunt)

  new_root = Spectre(ghost_id=generate_gids(1)[0], is_root=True, is_active=True, haunt=haunt)
  db.session.add(new_root)

  db.session.commit()

  session['id'] = new_root.ghost_id
  return redirect(url_for('views.haunt'))

@views.route('/haunt')
def haunt():
  ghost_id = session.get('id')

  if not ghost_id:
    flash('You need to enter your ghost ID first', 'info')
    return redirect(url_for('views.home'))

  ghost = Spectre.query.filter_by(ghost_id=ghost_id).first()

  if not ghost:
    session.clear()
    flash('Saved ghost ID not found', 'warning')
    return redirect(url_for('views.home'))

  ghosts = Spectre.query.filter_by(haunt=ghost.haunt, is_active=True)

  ghosts = json.dumps([ghost.as_dict() for ghost in ghosts])

  return render_template('pages/haunt.html', ghosts=ghosts, id=ghost.id, ghost_id=ghost_id)

@views.route('/auth', methods=['POST'])
def auth():
  ghost_id = str(request.form.get('ghost_id')).upper()

  if not ghost_id:
    flash('You need to ender a ghost ID', 'info')
    return redirect(url_for('views.home'))

  ghost = Spectre.query.filter_by(ghost_id=ghost_id).first()

  if not ghost:
    flash('Ghost ID not found', 'warning')
    return redirect(url_for('views.home'))

  if not ghost.is_active:
    ghost.is_active = True
    db.session.commit()

  session['id'] = ghost.ghost_id

  return redirect(url_for('views.haunt'))


@views.route('/haunt/download')
def download_ghosts():
  ghost_id = session.get('id')

  if not ghost_id:
    flash('You need to enter your ghost ID first', 'info')
    return redirect(url_for('views.home'))

  ghost = Spectre.query.filter_by(ghost_id=ghost_id).first()

  if not ghost:
    session.clear()
    flash('Saved ghost ID not found', 'warning')
    return redirect(url_for('views.home'))

  ghost_ids = generate_gids(2)

  for ghost_id in ghost_ids:
    new_spectre = Spectre(ghost_id=ghost_id, haunt=ghost.haunt, parent=ghost)
    db.session.add(new_spectre)

  db.session.commit()

  ghost_pdf = generate(ghost_ids)

  return send_file(ghost_pdf, attachment_filename='ghosts.pdf', as_attachment=True, cache_timeout=0)
