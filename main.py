from threading import Thread, ThreadError
from tkinter import Tk, Menu
from tkinter.messagebox import showinfo
from os import getpid
from os.path import abspath
import subprocess

from ModulosFront.configs import Configs
from ModulosFront.construtor import Construtor
from ModulosFront.tela_login import Logon


class Modulos:
    modulos_iniciados = dict()

    def cadastro_clientes(self):
        path = abspath('./ModulosFront/cadastro_clientes.py')
        nome_servico = 'cad_cli'
        if not self.modulos_iniciados.get(nome_servico, False):
            self.abrir_modulo(path, nome_servico)
        elif not self.modulos_iniciados[nome_servico].is_alive():
            self.abrir_modulo(path, nome_servico)
        else:
            showinfo('Já iniciado', 'Módulo já em execução')

    def cadastro_produtos(self):
        path = abspath('./ModulosFront/cadastro_produtos.py')
        nome_servico = 'cad_prod'
        if not self.modulos_iniciados.get(nome_servico, False):
            self.abrir_modulo(path, nome_servico)
        elif not self.modulos_iniciados[nome_servico].is_alive():
            self.abrir_modulo(path, nome_servico)
        else:
            showinfo('Já iniciado', 'Módulo já em execução')

    def cadastro_servicos(self):
        path = abspath('./ModulosFront/cadastro_servicos.py')
        nome_servico = 'cad_serv'
        if not self.modulos_iniciados.get(nome_servico, False):
            self.abrir_modulo(path, nome_servico)
        elif not self.modulos_iniciados[nome_servico].is_alive():
            self.abrir_modulo(path, nome_servico)
        else:
            showinfo('Já iniciado', 'Módulo já em execução')

    def controle_estoque(self):
        path = abspath('./ModulosFront/controle_estoque.py')
        nome_servico = 'cont_estq'
        if not self.modulos_iniciados.get(nome_servico, False):
            self.abrir_modulo(path, nome_servico)
        elif not self.modulos_iniciados[nome_servico].is_alive():
            self.abrir_modulo(path, nome_servico)
        else:
            showinfo('Já iniciado', 'Módulo já em execução')

    def vendas(self):
        path = abspath('./ModulosFront/vendas.py')
        nome_servico = 'vendas'
        if not self.modulos_iniciados.get(nome_servico, False):
            self.abrir_modulo(path, nome_servico)
        elif not self.modulos_iniciados[nome_servico].is_alive():
            self.abrir_modulo(path, nome_servico)
        else:
            showinfo('Já iniciado', 'Módulo já em execução')

    def ranking_clientes(self):
        path = abspath('./ModulosFront/ranking_clientes.py')
        nome_servico = 'rnk_cli'
        if not self.modulos_iniciados.get(nome_servico, False):
            self.abrir_modulo(path, nome_servico)
        elif not self.modulos_iniciados[nome_servico].is_alive():
            self.abrir_modulo(path, nome_servico)
        else:
            showinfo('Já iniciado', 'Módulo já em execução')

    def paretto(self):
        pass

    def clientes_regiao(self):
        pass

    def compras_periodo(self):
        pass

    def abrir_modulo(self, path, nome_processo):
        caminho = f'py {path} --user {self.user} --logado {self.logado}'
        modulo = Thread(target = lambda: subprocess.call(caminho), daemon = False)
        modulo.start()

        self.modulos_iniciados[nome_processo] = modulo


class Interface(Modulos, Configs, Logon):
    logado = False
    menus_criados = list()
    user = None
    configs_path = abspath('./Configs/configs.json')

    def __init__(self):
        Configs.__init__(self, self.configs_path)
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

        root.protocol(root.wm_protocol()[0], self.fechar_programas)

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
        subprocess.call(f'taskkill /F /PID {pid} /T', shell = True)


if __name__ == '__main__':
    Interface()
