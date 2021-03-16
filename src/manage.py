from src.text_extraction import TextExtraction
from src.organize_directory import OrganizeDirectory
from src.process_image import ProcessImage
from termcolor import colored
from operator import length_hint
import os

os.system("")

class Manage:

    def __init__(self):
        super().__init__()
        self.text_extraction = TextExtraction()
        self.organize_directory = OrganizeDirectory()
        self.process_image = ProcessImage()

    def set_lang(self, arg):
        self.text_extraction.set_lang(arg)
    
    def set_directory_image(self, directory):
        paths = self.organize_directory.get_path_images(directory)
        for i, image_path in enumerate(paths):
            print('###', i + 1)
            self.__generate_text(image_path)

    def set_image_to_text(self, path):
        self.__generate_text(path)

    def __generate_text(self, image_path):
        print('>>>>>>', image_path)
        print(colored('Extraíndo texto...', 'yellow'))
        self.process_image.remove_noise_and_smooth(image_path)
        text = self.text_extraction.image_to_text(image_path)
        self.organize_directory.write_file(text, image_path)
        print(colored('Finalizado com sucesso', 'green'))
    
    def join_all_txt_files(self, path):
        self.organize_directory.join_files(path)
        print(colored('Junção de arquivos finalizado com sucesso', 'green'))