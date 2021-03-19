import pytesseract
from PIL import Image
import platform

class TextExtraction:

    TESSPATH = 'Tesseract-OCR/tesseract.exe'

    def __init__(self):
        if platform.system() == 'Windows':
            pytesseract.pytesseract.tesseract_cmd = self.TESSPATH
        self.set_lang()
        
    def set_lang(self, lang='por'):
        self.language = lang

    def image_to_text(self, path):
        image = Image.open(path)
        return pytesseract.image_to_string(image, lang=self.language)
    
    def image_cv2_to_text(self, image):
        return pytesseract.image_to_string(image, lang=self.language)

    #@staticmethod
    

