from src.manage import Manage
import argparse
import webbrowser

class Arguments:

    manage = Manage()

    def __init__(self):
        super().__init__()
        self.add_argument()
        self.check_arguments()

    def add_argument(self):
        self.parser = argparse.ArgumentParser(prog='Information Extract OCR', conflict_handler='resolve', description='sum the integers at the command line')
        self.parser.add_argument('--output', '-o', help='foo help')
        self.parser.add_argument('--image', '-i', help='foo help')
        self.parser.add_argument('-lang', help='Inserir imagem')
        self.parser.add_argument('--directory', '-d', help='Inserir imagem')
        self.parser.add_argument('--join', help='Inserir imagem')
        self.parser.add_argument('--version', '-v', action='version', version='%(prog)s 0.2', help='Inserir imagem')
        self.parser.add_argument('code', nargs='?', help='Inserir imagem')


    def check_arguments(self):
        args = self.parser.parse_args()
        if (args.lang):
            self.manage.set_lang(args.lang)
        if (args.image):
            self.manage.set_image_to_text(args.image)
        if (args.directory):
            self.manage.set_directory_image(args.directory)
        if (args.output):
            print()
        if (args.join):
            self.manage.join_all_txt_files(args.join)
        if (args.code):
            print('O código fonte está em: https://github.com/SavioAndres/InformationExtractOCR')
            webbrowser.open('https://github.com/SavioAndres/InformationExtractOCR')

    
    def get_args(self):
        return self.parser.parse_args()


if __name__ == '__main__':
    Arguments()

#Criar Thread