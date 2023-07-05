from PIL import Image, ImageDraw, ImageFilter
import os
def makevideo(img_path):
    background = Image.open(img_path).resize([1920, 1080]).filter(ImageFilter.BoxBlur(80))
    foreground = Image.open(img_path)
    bg_w, bg_h = background.size
    img_w, img_h = foreground.size
    offset = ((bg_w - img_w) // 2, (bg_h - img_h) // 2)
    background.paste(foreground, offset)
    file = background.save('./imageprocessed.jpeg')
    return os.getcwd() + '\\imageprocessed.jpeg'