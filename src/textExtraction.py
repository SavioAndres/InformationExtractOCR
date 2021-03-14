import pytesseract
from PIL import Image
import configparser

class TextExtraction:

    def __init__(self):
        super().__init__()
        self.tesseract()

    def tesseract(self):
        config = configparser.ConfigParser()
        config.read('config.ini')
        tesseract_path = config.get('paths', 'tesseract_path')
        pytesseract.pytesseract.tesseract_cmd = 'Tesseract-OCR/tesseract.exe'

    def setImage(self, path):
        self.image = Image.open(path)
    
    def getText(self):
        return pytesseract.image_to_string(self.image, lang='por')
