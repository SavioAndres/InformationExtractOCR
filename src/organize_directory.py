from termcolor import colored
import os
from src.text_extraction import TextExtraction

class OrganizeDirectory:

    text_extraction = TextExtraction()

    def __init__(self):
        super().__init__()
    
    def get_path_files(self, path):
        return os.listdir(path)

    def set_directory_image(self, path):
        directory = os.listdir(path)
        for image_path in directory:
            text = self.text_extraction.image_to_text(image_path)
            self.write_file(text, image_path)
    
    def write_file(self, text, name='a'):
        file_text = open('{}.txt'.format(name), 'w')
        file_text.write(text)
        file_text.close()
        print(colored('Sucess', 'green'))