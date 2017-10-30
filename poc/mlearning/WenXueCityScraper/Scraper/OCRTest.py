try:
    import Image
except ImportError:
    from PIL import Image
import pytesseract

tessdata_dir_config = './'
pytesseract.pytesseract.tesseract_cmd = './'
# Include the above line, if you don't have tesseract executable in your PATH
# Example tesseract_cmd: 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract'

im = Image.open('Screen.png')
print im
pytesseract.image_to_string(im)
#print(pytesseract.image_to_string(Image.open('./Screen.png')))
#print(pytesseract.image_to_string(Image.open('test-european.jpg'), lang='fra'))

