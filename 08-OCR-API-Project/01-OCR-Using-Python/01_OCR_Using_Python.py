# pip install pytesseract

import pytesseract

# for Windows
pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

img_path = 'test3.jpg'
lang = 'eng'
text = pytesseract.image_to_string(img_path, lang=lang)

print(text)