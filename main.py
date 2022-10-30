from threading import Thread
from tkinter import Tk, Menu
from tkinter.messagebox import showinfo
from os import getpid
from os.path import abspath
import subprocess

from ModulosFront.configs import Configs
from ModulosFront.construtor import Construtor
from ModulosFront.tela_login import Logon


class Modulos:
    def cadastro_clientes(self):
        try:
            if self.cad_cli.is_alive():
                raise showinfo('Já iniciado', 'Módulo já em execução')
        except AttributeError:
            pass
        path = abspath('ModulosFront/cadastro_clientes.py')
        self.cad_cli = Thread(target = lambda: subprocess.call(self.abrir_modulo(path)), daemon = False)
        self.cad_cli.start()

    def cadastro_produtos(self):
        try:
            if self.cad_prod.is_alive():
                raise showinfo('Já iniciado', 'Módulo já em execução')
        except AttributeError:
            pass
        path = abspath('ModulosFront/cadastro_produtos.py')
        comando = f'py {path} --user {self.user} --logado {self.logado}'
        self.cad_prod = Thread(target = lambda: subprocess.call(self.abrir_modulo(path)), daemon = False)
        self.cad_prod.start()

    def cadastro_servicos(self):
        pass

    def controle_estoque(self):
        pass

    def vendas(self):
        pass

    def ranking_clientes(self):
        pass

    def paretto(self):
        pass

    def clientes_regiao(self):
        pass

    def compras_periodo(self):
        pass

    def abrir_modulo(self, path):
        return f'py {path} --user {self.user} --logado {self.logado}'


class Interface(Modulos, Configs, Logon):
    logado = False
    menus_criados = list()
    user = None

    def __init__(self):
        self.inicia_configs()
        self.inicia_root()
        self.inicia_menu()
        self.root.after(100, self.login, *())
        self.root.mainloop()

    # Inicia a tela com nome da empresa
    def inicia_root(self):
        root = Tk()
        root.title(self.nome_da_empresa)
        largura_tela = int(root.winfo_screenwidth() / 1.2)
        altura_tela = int(root.winfo_screenheight() / 1.2)
        root.geometry(f'{largura_tela}x{altura_tela}+50+30')
        root.configure(**self.root_params)

        root.bind('<Destroy>', lambda e: self.fechar_programas())

        self.root = root

    def inicia_menu(self):
        menu_bar = Menu(master = self.root)

        menus = {
            'Cadastros': (
                ('Cadastro de clientes', self.cadastro_clientes),
                ('Cadastro de produtos', self.cadastro_produtos),
                ('Cadastro de serviços', self.cadastro_servicos),
                ('Controle de estoque', self.controle_estoque),
            ),
            'Vendas': (
                ('Vendas', self.vendas),
            ),
            'Relatórios': (
                ('Clientes por região', self.clientes_regiao),
                ('Compras por periodo', self.compras_periodo),
                ('Ranking de clientes', self.ranking_clientes),
                ('Paretto', self.paretto),
            )
        }

        for menu_superior in menus:
            novo_menu = Menu(master = menu_bar, tearoff = 0)
            menu_bar.add_cascade(label = menu_superior, menu = novo_menu, state = 'disabled')
            self.menus_criados.append(menu_superior)

            for menu_inferior, comando in menus[menu_superior]:
                novo_menu.add_command(label = menu_inferior, command = comando)

        self.root.config(menu = menu_bar)
        self.menu_bar = menu_bar

    @staticmethod
    def fechar_programas():
        pid = getpid()
        subprocess.call(f'taskkill /PID {pid} /T', shell = True)


if __name__ == '__main__':
    Interface()
