#!/usr/bin/env python
from PIL import Image
from models.receipt import Receipt
import pytesseract

print(Receipt('./kimchi_api/images/image_1.jpeg').date)