import pytesseract
from PIL import Image

class TextExtraction:

    TESSPATH = 'Tesseract-OCR/tesseract.exe'

    def __init__(self):
        super().__init__()
        pytesseract.pytesseract.tesseract_cmd = self.TESSPATH
        self.set_lang()
        
    def set_lang(self, lang='por'):
        self.language = lang

    def image_to_text(self, path):
        image = Image.open(path)
        return pytesseract.image_to_string(image, lang=self.language)

    #@staticmethod
    
