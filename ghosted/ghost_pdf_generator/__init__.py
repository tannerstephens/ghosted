from ghosted.routes.ghost_api import get_ghost
from PIL import Image, ImageDraw, ImageFont
from ..extensions import ghost_generator
import os
import io

dir_path = os.path.dirname(os.path.realpath(__file__))

fnt = ImageFont.truetype(dir_path + '/ssp.ttf', 50)

def generate(gids):
  im = Image.open(dir_path + '/ghosting.png')
  im = im.convert("RGB")
  draw = ImageDraw.Draw(im)

  draw.text((440,899), gids[0], font=fnt, fill=(0,0,0,255))
  draw.text((437,2006), gids[1], font=fnt, fill=(0,0,0,255))

  def get_ghost(gid, resize=2.2):
    ghost = ghost_generator.generate_ghost(gid)
    return ghost.resize((int(ghost.width/resize), int(ghost.height/resize)))

  ghost0 = get_ghost(gids[0])
  ghost1 = get_ghost(gids[1])

  im.paste(ghost0, (800,50), ghost0)
  im.paste(ghost1, (800,1197), ghost1)


  output = io.BytesIO()

  im.save(output, "PDF", resolution=100.0)

  output.seek(0)

  return output
