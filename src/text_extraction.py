import pytesseract
from PIL import Image
from src.organize_directory import OrganizeDirectory

class TextExtraction:

    TESSPATH = 'Tesseract-OCR/tesseract.exe'
    organize_directory = OrganizeDirectory()

    def __init__(self):
        super().__init__()
        pytesseract.pytesseract.tesseract_cmd = self.TESSPATH
        
        self.set_lang()
        
    def set_lang(self, lang='por'):
        self.language = lang

    def image_to_text(self, path):
        self.image = Image.open(path)
        return pytesseract.image_to_string(self.image, lang=self.language)

    #@staticmethod
    def set_image_to_text(self, path):
        text = self.image_to_text(path)
        self.organize_directory.write_file(text)

