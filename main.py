from src.arguments import Arguments
from src.textExtraction import TextExtraction

class Main:

    def __init__(self):
        super().__init__()
        args = Arguments()
        textE = TextExtraction()
        textE.setImage(args.getArgs().i)
        print(textE.getText())

Main()