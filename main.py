from src.manage import Manage
import argparse

class Arguments:

    manage = Manage()

    def __init__(self):
        super().__init__()
        self.add_argument()
        self.check_arguments()

    def add_argument(self):
        self.parser = argparse.ArgumentParser(prog='PROG', conflict_handler='resolve', description='sum the integers at the command line')
        self.parser.add_argument('--output', help='foo help')
        self.parser.add_argument('-o', help='foo help')
        self.parser.add_argument('--image', help='foo help')
        self.parser.add_argument('-i', help='Inserir imagem')
        self.parser.add_argument('-l', help='Inserir imagem')
        self.parser.add_argument('-lang', help='Inserir imagem')
        self.parser.add_argument('-d', help='Inserir imagem')
        self.parser.add_argument('--directory', help='Inserir imagem')

    def check_arguments(self):
        args = self.parser.parse_args()
        if (args.l or args.lang):
            self.manage.set_lang(args.l or args.lang)
        if (args.i or args.image):
            self.manage.set_image_to_text(args.i or args.image)
        if (args.d or args.directory):
            self.manage.set_directory_image(args.d or args.directory)
        if (args.o or args.output):
            print()

    
    def get_args(self):
        return self.parser.parse_args()


if __name__ == '__main__':
    Arguments()