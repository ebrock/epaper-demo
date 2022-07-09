import sys
sys.path.insert(1, "lib")

from datetime import datetime
from datetime import date
import time

import epd2in13_V2
from PIL import Image, ImageDraw, ImageFont

epd = epd2in13_V2.EPD() # get the display
epd.init(epd.FULL_UPDATE)
print("Clear...")
epd.Clear(0xFF)         # clear the display

def printToDisplay(string):
    today = date.today()
    printToday = today.strftime("%B %d, %Y")

    HBlackImage = Image.new('1', (epd2in13_V2.EPD_HEIGHT, epd2in13_V2.EPD_WIDTH), 255)

    draw = ImageDraw.Draw(HBlackImage)
    font = ImageFont.load_default()
    font_two = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeMonoBold.ttf", 20)
    font_three = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeMonoBold.ttf", 14)

    draw.text((50, 50), string, font=font_two, fill=0)
    draw.text((0, 0), printToday, font=font_three, fill=0)

    epd.display(epd.getbuffer(HBlackImage))
    epd.displayPartBaseImage(epd.getbuffer(HBlackImage))
    epd.init(epd.PART_UPDATE)

    while (True):
        draw.rectangle((120, 80, 220, 105), fill = 255)
        draw.text((120, 80), time.strftime('%I:%M %p'), font = font_three, fill = 0)
        epd.displayPartial(epd.getbuffer(HBlackImage))

def clearDisplay():
    epd.Clear(0xFF)

printToDisplay("Raspberry Pi")
# clearDisplay()
