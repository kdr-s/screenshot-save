from PIL import ImageGrab, ImageChops, Image
from datetime import datetime
from time import sleep
from os import makedirs
from os.path import expanduser

last_im = Image.new("RGB", (512, 512), (128, 128, 128))
folder = expanduser("~") + "/Pictures/Screenshots/"
# Ctrl = 0x11
makedirs(folder, exist_ok=True)

while True:
    im = ImageGrab.grabclipboard()
    if isinstance(im, Image.Image):
        # ２つの画像が同一の場合ImageChops.differenceはすべて0の画像を返す
        if ImageChops.difference(im, last_im).getbbox() != None:
            im.save(folder + datetime.now().strftime("%Y%m%d-%H%M%S") + ".png")
            last_im = im
    sleep(1)
