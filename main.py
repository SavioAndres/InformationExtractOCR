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
        self.parser.add_argument('-l', '--lang', choices=['por', 'eng'], help='Inserir lingua do texto da imagem')
        self.parser.add_argument('-i', '--image', action='append', help='Caminho da imagem de entrada')
        self.parser.add_argument('-d', '--dir', help='Caminho do diretório de entrada das imagens')
        self.parser.add_argument('-o', '--out', help='Caminho do diretório de saída dos textos extraídos')
        self.parser.add_argument('-oi', '--outimage', help='Caminho do diretório de saída das imagens processadas')
        self.parser.add_argument('-j', '--join', help='Criar um novo arquivo de texto com todos os textos \
                                    extraídos dos arquivos de um determinado diretório')
        self.parser.add_argument('-v', '--version', help='Versão do software', action='version', version='%(prog)s Version 0.2')
        self.parser.add_argument('code', nargs='?', help='Código fonte')

    def check_arguments(self):
        args = self.parser.parse_args()
        if (args.lang):
            self.manage.set_lang(args.lang)
        if (args.image):
            self.manage.set_image(args.image)
        if (args.dir):
            self.manage.set_directory_images(Path(args.dir))
        if (args.out):
            self.manage.set_directory_out_text(Path(args.out))
        if (args.outimage):
            self.manage.set_directory_out_image(Path(args.outimage))
        if (args.join):
            self.manage.join_all_txt_files(Path(args.join))
        if (args.code):
            print('O código fonte está em: https://github.com/SavioAndres/InformationExtractOCR')
            webbrowser.open('https://github.com/SavioAndres/InformationExtractOCR')

if __name__ == '__main__':
    Arguments()