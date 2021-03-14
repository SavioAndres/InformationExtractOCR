import argparse

class Arguments:

    def __init__(self):
        super().__init__()
        self.add_argument()

    def add_argument(self):
        self.parser = argparse.ArgumentParser(prog='PROG', conflict_handler='resolve', description='sum the integers at the command line')
        self.parser.add_argument('--foo', help='foo help')
        self.parser.add_argument('-f', help='foo help')
        self.parser.add_argument('-i', help='Inserir imagem')
    
    def getArgs(self):
        return self.parser.parse_args()
