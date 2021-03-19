from glob import glob
import os
import pathlib
from unicodedata import normalize
from PIL import Image
from pathlib import Path

class OrganizeDirectory:
    
    def get_path_files(self, path):
        return os.listdir(path)
    
    def write_file(self, text, name='a'):
        file_text = open('{}.txt'.format(name), 'w')
        file_text.write(text)
        file_text.close()

    def convert_to_jpg(self, path):
        png = list(pathlib.Path(path).glob('**/*.png'))
        png_jpeg = png + list(pathlib.Path(path).glob('**/*.jpeg'))
        
        for img in png_jpeg:
            path_img = Path(str(img))
            img = Image.open(path_img)
            img = img.convert('RGB')
            img.save(path_img.with_suffix('.jpg'))
            os.remove(path_img)

    def get_path_images(self, path):
        unaccented_path = self.remove_accents_directories_files(path)
        self.convert_to_jpg(unaccented_path)
        lista_arqs = pathlib.Path(unaccented_path).glob('**/*.jpg')
        #print(lista_arqs)
        return lista_arqs
    
    def remove_accents_directories_files(self, path):
        unaccented_path = self.remove_accents_directories(path)
        lista_arqs = os.listdir(unaccented_path)
        for arq in lista_arqs:
            rename_arq = normalize('NFKD', arq).encode('ASCII', 'ignore').decode('ASCII')
            os.rename(unaccented_path + '/' + arq, unaccented_path + '/' + rename_arq)
        return unaccented_path
    
    def remove_accents_directories(self, path):
        path_dirs, unaccented_path_dirs = self.path_split_unaccented(path)
        
        concatenated_path = ''
        concatenated_path_unaccented = ''
        for i, _ in enumerate(path_dirs):
            concatenated_path = concatenated_path_unaccented + path_dirs[i] + '/'
            concatenated_path_unaccented += unaccented_path_dirs[i] + '/'

            if path_dirs[i] != unaccented_path_dirs[i]:
                os.rename(concatenated_path[:-1], concatenated_path_unaccented[:-1])
        
        return concatenated_path_unaccented[:-1]

    def join_files(self, path):
        paths = glob('{0}/*.txt'.format(path))
        arq = open(path + '/resultado.txt', 'w')
        text = ''
        for p in paths:
            text += open(p, 'r').read()
        arq.write(text)
        arq.close()

    def path_split_unaccented(self, path):
        unaccented_path = normalize('NFKD', path).encode('ASCII', 'ignore').decode('ASCII')
        
        path = os.path.normpath(path)
        path_dirs = path.split(os.sep)

        unaccented_path = os.path.normpath(unaccented_path)
        unaccented_path_dirs = unaccented_path.split(os.sep)

        return path_dirs, unaccented_path_dirs