from src.manage import Manage
import argparse
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
        self.parser.add_argument('-si', '--saveimage', help='Salvar imagem processada [true ou false]')
        self.parser.add_argument('-init', '--init', type=int, help='Número de início para varrer as imagens')
        self.parser.add_argument('-i', '--image', action='append', help='Caminho da imagem de entrada')
        self.parser.add_argument('-d', '--dir', help='Caminho do diretório de entrada das imagens')
        self.parser.add_argument('-o', '--out', help='Caminho do diretório de saída dos textos extraídos')
        self.parser.add_argument('-oi', '--outimage', help='Caminho do diretório de saída das imagens processadas')
        self.parser.add_argument('-v', '--version', help='Versão do software', action='version', 
                                    version='%(prog)s Version 1.0 [https://github.com/SavioAndres/InformationExtractOCR]')

    def check_arguments(self):
        args = self.parser.parse_args()
        if (args.lang):
            self.manage.set_lang(args.lang)
        if (args.saveimage):
            self.manage.set_is_save_image_process(args.saveimage)
        if (args.init):
            self.manage.set_value_init(args.init)
        if (args.outimage):
            self.manage.set_directory_out_image(Path(args.outimage))
        if (args.out):
            self.manage.set_directory_out_text(Path(args.out))
        if (args.image):
            self.manage.set_image(args.image)
        if (args.dir):
            self.manage.set_directory_images(Path(args.dir))

if __name__ == '__main__':
    Arguments()