from PIL import Image, ImageDraw, ImageFont
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

  output = io.BytesIO()

  im.save(output, "PDF", resolution=100.0)

  output.seek(0)

  return output
