import pytesseract
import asyncio

# for Windows
pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

async def read_image(img_path, lang='eng'):
    try:
        text = pytesseract.image_to_string(img_path, lang=lang)
        # we pause the execution for just 2 seconds. At this point, your complex 
        # IO operations can also take place. This is the point where the coroutine 
        # switching will take place.
        await asyncio.sleep(2)
        return text
    except:
        return "[ERROR] Unable to process file: {0}".format(img_path)