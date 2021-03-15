from glob import glob
from os import listdir
import pathlib

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
        lista_arqs = pathlib.Path(path).glob('**/*.jpg')
        print(lista_arqs)
        return lista_arqs