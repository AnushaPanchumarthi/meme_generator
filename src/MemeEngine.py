"""The Meme Engine is responsible for manipulating and drawing text onto images."""

from PIL import Image,ImageDraw, ImageFont
from QuoteEngine.QuoteModel import QuoteModel
import os
import random


class MemeEngine():
    text_margin = 2 

    def __init__(self, out_path):
        self.out_path = out_path
        self.number = 1
        if not os.path.exists(out_path):
            os.makedirs(out_path)

    def make_meme(self, img_path, body, author, crop=None, width = 500):
        try:
            img = Image.open(img_path)
            out_file = os.path.join(self.out_path,f"meme-{self.number}.jpg")
            self.number += 1

            if crop is not None:
                img = img.crop(crop)

            if width is not None:
                ratio = width/float(img.size[0])
                height = int(ratio*float(img.size[1]))
                img = img.resize((width, height), Image.NEAREST)

            if body is not None:
                draw = ImageDraw.Draw(img)
                font = ImageFont.truetype('./_data/LilitaOne-Regular.ttf', size=20)
                quote_str = str(QuoteModel(body, author))

                # try to avoid text going outside the image
                margin = min(type(self).text_margin, img.width, img.height)
                text_width, text_height = draw.textsize(quote_str, font=font)
                text_x = random.randint(margin, max(margin, img.width - text_width - margin))
                text_y = random.randint(margin, max(margin, img.height - text_height - margin))

                draw.text((text_x, text_y), str(QuoteModel(body, author)), font=font, fill='white', stroke_fill='black')
            

            img.save(out_file)
        
        except:
            raise Exception ('making meme is not implemented')
        
        return out_file
            
