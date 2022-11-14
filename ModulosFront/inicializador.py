from argparse import ArgumentParser


class Argumentos:
    @staticmethod
    def argumentos():
        parser = ArgumentParser(exit_on_error = True, add_help = False, allow_abbrev = False)
        parser.add_argument('--user', default = None, required = True)
        parser.add_argument('--senha', default = None, required = True)
        parser.add_argument('--logado', default = None, required = True)
        return parser.parse_args()
