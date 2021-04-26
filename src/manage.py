from src.text_extraction import TextExtraction
from src.organize_directory import OrganizeDirectory
from src.process_image import ProcessImage
from termcolor import colored
import os
from pathlib import Path

os.system("")

class Manage:

    def __init__(self):
        self.text_extraction = TextExtraction()
        self.organize_directory = OrganizeDirectory()
        self.process_image = ProcessImage()

        self.path_input = None
        self.path_output_text = None
        self.path_output_image = None

        self.save_image_process = True

        self.value_init = 0

    # -lang
    def set_lang(self, arg):
        self.text_extraction.set_lang(arg)

    # --saveimage
    def set_is_save_image_process(self, arg):
        if arg.lower() in {'false', 'f', '0', 'no', 'n'}:
            self.save_image_process = False

    # --init
    def set_value_init(self, arg):
        self.value_init = arg

    # --image
    def set_image(self, paths):
        size_list = len(paths) - 1
        for i, path in enumerate(paths[self.value_init:], start=self.value_init):
            print(colored('Nº {0}/{1} >>>>>>\t{2}'.format(i, size_list, path), 'blue'))
            _path_output_text = self.path_output_text
            _path_output_image = self.path_output_image

            if _path_output_text == None: _path_output_text = path + ' text'
            if _path_output_image == None: _path_output_image = path + ' image'

            path_unaccented, accentuation_removed = self.organize_directory.remove_accents_directories(Path(path))
            if accentuation_removed: print(colored('Acentuação do diretório/imagem retirada', 'blue'))
            
            print(colored('Processando imagem...', 'yellow'))
            image = self.process_image.process(path_unaccented)
            if self.save_image_process:
                path_out_image = self.organize_directory.generate_directory_name(path, self.path_input, _path_output_image)
                self.process_image.create_image(image, path_out_image)
            
            print(colored('Extraíndo texto...', 'yellow'))
            text = self.text_extraction.image_to_text(image)
            path_out_text = self.organize_directory.generate_directory_name(path, self.path_input, _path_output_text)
            self.organize_directory.write_file(text, path_out_text)
            
            print(colored('Finalizado com sucesso', 'green'))
    
    # --dir
    def set_directory_images(self, path):
        self.path_input = path
        self.__create_exit_paths(path)

        list_paths_images = list()
        for path, _, name_file in os.walk(os.path.abspath(path)):
            if os.path.basename(path) != 'arquivo':
                for name in name_file:
                    if name.endswith('.jpg'):
                        list_paths_images.append(path + '/' + name)
        self.set_image(list_paths_images)

    # --out
    def set_directory_out_text(self, path):
        self.path_output_text = path
        if self.path_output_image == None: self.path_output_image = path

    # --outimage
    def set_directory_out_image(self, path):
        self.path_output_image = path

    # Criar caminhos de saída
    def __create_exit_paths(self, path):
        if self.path_output_image == None:
            self.path_output_image = os.path.dirname(path) + '/' + os.path.basename(path) + ' image'
        if self.path_output_text == None:
            self.path_output_text = os.path.dirname(path) + '/' + os.path.basename(path) + ' text'
