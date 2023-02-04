from functools import cached_property
import re
import dateparser
from PIL import Image

import pytesseract

class Receipt(object):
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.raw = pytesseract.image_to_string(Image.open(filename))
        print(self.raw)
        self.merchant = None
        self.total = None
        self.tip = None
        self.tax = None
        self.lines = [l.lower() for l in self.raw.split('\n') if l.strip()]
        
    @cached_property
    def date(self):
        for line in self.lines:
            print(line)
            match = re.search('((0|1)\d{1})\/((0|1|2)\d{1})\/((19|20)\d{0,2})', line)
            if match:
                print(match)
                date_str = match.group(0).replace(' ', '')
                print(date_str)
                try:
                    return dateparser.parse(date_str).date()
                except:
                    continue