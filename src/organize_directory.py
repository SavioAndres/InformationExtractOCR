from glob import glob
import os
import pathlib
from unicodedata import normalize

class OrganizeDirectory:

    def __init__(self):
        super().__init__()
    
    def get_path_files(self, path):
        return os.listdir(path)
    
    def write_file(self, text, name='a'):
        file_text = open('{}.txt'.format(name), 'w')
        file_text.write(text)
        file_text.close()

    def get_path_images(self, path):
        #path_image = glob('{0}/.'.format(path))
        #path_image.extend(glob('{0}/*.jpg'.format(path)))
        #path_image.extend(glob('{0}/*.jpeg'.format(path)))
        #path_image.extend(glob('{0}/*.png'.format(path)))
        
        unaccented_path = self.remove_accents_directories_files(path)
        lista_arqs = pathlib.Path(unaccented_path).glob('**/*.jpg')
        #print(lista_arqs)
        return lista_arqs
    
    def remove_accents_directories_files(self, path):
        unaccented_path = path #normalize('NFKD', path).encode('ASCII', 'ignore').decode('ASCII')
        #os.rename(path, unaccented_path)
        lista_arqs = os.listdir(unaccented_path)
        for arq in lista_arqs:
            rename_arq = normalize('NFKD', arq).encode('ASCII', 'ignore').decode('ASCII')
            os.rename(unaccented_path + '/' + arq, unaccented_path + '/' + rename_arq)
        return unaccented_path
    
    def remove_accents_files(self, path):
        path = str(path)
        unaccented_path = normalize('NFKD', path).encode('ASCII', 'ignore').decode('ASCII')
        print('llkjhhhhh>>> ', path, 'oooo',unaccented_path)
        os.rename(path, unaccented_path)
        return unaccented_path

    def join_files(self, path):
        paths = glob('{0}/*.txt'.format(path))
        arq = open(path + '/resultado.txt', 'w')
        text = ''
        for p in paths:
            text += open(p, 'r').read()
        arq.write(text)
        arq.close()