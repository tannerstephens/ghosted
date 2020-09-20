from PIL import Image

from glob import glob
from hashlib import md5
from io import BytesIO
from os import path

class GhostGenerator:
  def __init__(self, app=None):
    if app:
      self.init_app(app)
    self.app = app

  def init_app(self, app):
    self.app = app
    app.config['ghost_files'] = self._detect_files()

  def _detect_files(self):
    CURRENT_DIR = path.dirname(path.abspath(__file__))

    return {
      'base': Image.open(f'{CURRENT_DIR}/ghost/base.png'),
      'eyes': self._load_images(glob(f'{CURRENT_DIR}/ghost/eyes/*.png')),
      'mouths': self._load_images(glob(f'{CURRENT_DIR}/ghost/mouths/*.png')),
      'necks': self._load_images(glob(f'{CURRENT_DIR}/ghost/necks/*.png'))
    }

  def _load_images(self, images):
    return [Image.open(image) for image in images]

  def generate_ghost(self, s):
    files = self.app.config['ghost_files']

    h = md5(s.encode()).hexdigest()

    eyes_hex = h[:16]
    mouth_hex = h[16:]
    neck_hex = h[8:16]

    eyes_index = int(eyes_hex, 16) % len(files['eyes'])
    mouth_index = int(mouth_hex, 16) % len(files['mouths'])
    neck_index = int(neck_hex, 16) % len(files['necks'])

    base = files['base'].copy()
    eyes = files['eyes'][eyes_index]
    mouth = files['mouths'][mouth_index]
    neck = files['necks'][neck_index]

    base.paste(eyes, (511,496), eyes)
    base.paste(mouth, (485,812), mouth)
    base.paste(neck, (485,1150), neck)

    return base

  def generate_ghost_io(self, s):
    io = BytesIO()
    self.generate_ghost(s).save(io, 'PNG')
    io.seek(0)
    return io
