from src.text_extraction import TextExtraction
from src.organize_directory import OrganizeDirectory
from termcolor import colored

class Manage:

    def __init__(self):
        super().__init__()
        self.text_extraction = TextExtraction()
        self.organize_directory = OrganizeDirectory()

    def set_lang(self, arg):
        self.text_extraction.set_lang(arg)
    
    def set_directory_image(self, arg):
        paths = self.organize_directory.get_path_images(arg)
        for image_path in paths:
            self.__generate_text(image_path)

    def set_image_to_text(self, path):
        self.__generate_text(path)

    def __generate_text(self, image_path):
        print(image_path)
        print(colored('Extraíndo texto...', 'blue'))
        text = self.text_extraction.image_to_text(image_path)
        self.organize_directory.write_file(text, image_path)
        print(colored('Finalizado com sucesso', 'green'))