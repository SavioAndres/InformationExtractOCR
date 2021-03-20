from glob import glob
import os
import pathlib
from unicodedata import normalize
from PIL import Image
from pathlib import Path

class OrganizeDirectory:
    
    # Escreve o arquivo TXT com o texto extraído
    def write_file(self, text, name):
        file_text = open('{}.txt'.format(name), 'w')
        file_text.write(text)
        file_text.close()

    # Converte todas imagens png e jpeg em jpg no diretório escolhido
    def convert_to_jpg(self, path):
        png = list(pathlib.Path(path).glob('**/*.png'))
        png_jpeg = png + list(pathlib.Path(path).glob('**/*.jpeg'))
        
        for img in png_jpeg:
            path_img = Path(str(img))
            img = Image.open(path_img)
            img = img.convert('RGB')
            img.save(path_img.with_suffix('.jpg'))
            os.remove(path_img)

        return len(png_jpeg) != 0

    def get_path_images(self, path):
        unaccented_path, accentuation_removed = self.remove_accents_directories_files(path)
        was_converted = self.convert_to_jpg(unaccented_path)
        list_paths_images = pathlib.Path(unaccented_path).glob('**/*.jpg')
        return list_paths_images, accentuation_removed, was_converted
    
    # Passando o caminho de um diretório
    # Remove os acentos dos dos diretórios e subdiretórios até as imagens
    def remove_accents_directories_files(self, path):
        unaccented_path, accentuation_removed = self.remove_accents_directories(path)
        lista_arqs = os.listdir(unaccented_path)
        unaccented_path = str(unaccented_path)

        accented_file = False
        for arq in lista_arqs:
            rename_arq = normalize('NFKD', arq).encode('ASCII', 'ignore').decode('ASCII')
            accented_file = accented_file or (arq != rename_arq)
            os.rename(unaccented_path + '/' + arq, unaccented_path + '/' + rename_arq)

        return Path(unaccented_path), accentuation_removed or accented_file
    
    # Passando o caminho de uma imagem
    # Remove os acentos dos dos diretórios e subdiretórios
    def remove_accents_directories(self, path):
        list_path_dirs, list_unaccented_path_dirs = self.__path_split_unaccented(path)
        
        concatenated_path = ''
        concatenated_path_unaccented = ''
        for i, _ in enumerate(list_path_dirs):
            concatenated_path = concatenated_path_unaccented + list_path_dirs[i] + '/'
            concatenated_path_unaccented += list_unaccented_path_dirs[i] + '/'

            if list_path_dirs[i] != list_unaccented_path_dirs[i]:
                os.rename(concatenated_path[:-1], concatenated_path_unaccented[:-1])
        
        path_unaccented = Path(concatenated_path_unaccented[:-1])
        return path_unaccented, path != path_unaccented

    # Cria um novo arquivo de texto, sendo esse a junção de todos os arquivos de textos gerados
    def join_files(self, path):
        paths = glob('{0}/*.txt'.format(path))
        arq = open(path + '/resultado.txt', 'w')
        text = ''
        for p in paths:
            text += open(p, 'r').read()
        arq.write(text)
        arq.close()

    # def privado para gerar lista de strings do caminho do diretório/arquivo com e sem acentos
    def __path_split_unaccented(self, path):
        unaccented_path = normalize('NFKD', str(path)).encode('ASCII', 'ignore').decode('ASCII')
        
        path = os.path.normpath(path)
        list_path_dirs = path.split(os.sep)

        unaccented_path = os.path.normpath(unaccented_path)
        list_unaccented_path_dirs = unaccented_path.split(os.sep)

        return list_path_dirs, list_unaccented_path_dirs