from src.text_extraction import TextExtraction
from src.organize_directory import OrganizeDirectory
from src.process_image import ProcessImage
from termcolor import colored
import os

os.system("")

class Manage:

    def __init__(self):
        self.text_extraction = TextExtraction()
        self.organize_directory = OrganizeDirectory()
        self.process_image = ProcessImage()

    # -lang
    def set_lang(self, arg):
        self.text_extraction.set_lang(arg)
    
    # --dir
    def set_directory_images(self, directory):
        list_paths_images, accentuation_removed, was_converted = self.organize_directory.remove_accents_directories_files(directory)

        if accentuation_removed: print(colored('Acentuação do diretório e/ou imagem/ns retirada(s)', 'blue'))
        if was_converted: print(colored('Imagem/ns convertida/s para jpg', 'blue'))

        for i, image_path in enumerate(list_paths_images):
            print(colored('######\t{}'.format(i + 1), 'blue'))
            self.__generate_text(image_path)

    # --image
    def set_image(self, path):
        path, accentuation_removed = self.organize_directory.remove_accents_directories(path)
        if accentuation_removed: print(colored('Acentuação do diretório/imagem retirada', 'blue'))
        self.__generate_text(path)
    
    # --join
    def join_all_txt_files(self, path):
        self.organize_directory.join_files(path)
        print(colored('Junção de arquivos finalizado com sucesso', 'green'))

    def __generate_text(self, image_path):
        print(colored('>>>>>>\t{}'.format(image_path), 'blue'))
        print(colored('Processando imagem...', 'yellow'))
        image = self.process_image.process(image_path)
        print(colored('Extraíndo texto...', 'yellow'))
        text = self.text_extraction.image_to_text(image)
        self.organize_directory.write_file(text, image_path)
        print(colored('Finalizado com sucesso', 'green'))