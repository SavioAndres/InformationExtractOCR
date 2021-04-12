from src.manage import Manage
import argparse
import webbrowser
import platform
from pathlib import Path

class Arguments:

    manage = Manage()

    def __init__(self):
        title = 'Information Extract OCR (for {})'.format(platform.system())
        self.add_argument(title)
        self.check_arguments()

    def add_argument(self, title):
        self.parser = argparse.ArgumentParser(prog=title, conflict_handler='resolve')
        self.parser.add_argument('-l', '--lang', help='Inserir lingua do texto da imagem: [por, eng]')
        self.parser.add_argument('-i', '--image', help='Caminho da imagem de entrada')
        self.parser.add_argument('-d', '--dir', help='Caminho do diretório de entrada')
        self.parser.add_argument('-j', '--join', help='Criar um novo arquivo de texto com todos os textos \
                                    extraídos dos arquivos de um determinado diretório')
        self.parser.add_argument('-v', '--version', help='Versão do software', action='version', version='%(prog)s Version 0.2')
        self.parser.add_argument('code', nargs='?', help='Código fonte')

    def check_arguments(self):
        args = self.parser.parse_args()
        if (args.lang):
            self.manage.set_lang(args.lang)
        if (args.image):
            self.manage.set_image(Path(args.image))
        if (args.dir):
            self.manage.set_directory_images(Path(args.dir))
        if (args.join):
            self.manage.join_all_txt_files(Path(args.join))
        if (args.code):
            print('O código fonte está em: https://github.com/SavioAndres/InformationExtractOCR')
            webbrowser.open('https://github.com/SavioAndres/InformationExtractOCR')

if __name__ == '__main__':
    Arguments()