from flask import Blueprint, send_file
from ..extensions import ghost_generator, cache

ghost_api = Blueprint('ghost_api', __name__, url_prefix='/ghost')

@ghost_api.route('/<string:key>/ghost.png')
@ghost_api.route('/<string:key>.png')
@cache.memoize(3600)
def get_ghost(key):
  ghost = ghost_generator.generate_ghost_io(key)

  return send_file(ghost, mimetype='image/png')
