from threading import Thread
from tkinter import Tk, Menu
from tkinter.messagebox import showinfo
from os import getpid, system
from os.path import abspath

from ModulosFront.configs import Configs
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
        programa = 'venv\Scripts\python.exe'
        user = self.user
        senha = self.password
        logado = self.logado
        caminho = f'{programa} {path} --user {user} --senha {senha} --logado {logado}'
        modulo = Thread(target = lambda: system(caminho), daemon = False)
        modulo.start()

        self.modulos_iniciados[nome_processo] = modulo


class Interface(Modulos, Configs, Logon):
    user = None
    password = None
    perfil = None
    logado = False
    configs_path = abspath('./Configs/configs.json')

    def __init__(self):
        Configs.__init__(self, self.configs_path)
        self.inicia_root()
        self.root.after(100, lambda: Logon.__init__(self))
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
        self.root.config(menu = menu_bar)
        menus = self.consulta_menu_por_perfil

        for menu_superior in menus:
            novo_menu = Menu(master = menu_bar, tearoff = 0, name = menu_superior.lower())
            menu_bar.add_cascade(label = menu_superior, menu = novo_menu)
            novo_menu.winfo_name()

            for menu_inferior, comando in menus[menu_superior]:
                novo_menu.add_command(label = menu_inferior, command = comando)
        self.menu_bar = menu_bar

    @staticmethod
    def fechar_programas():
        pid = getpid()
        system(command = f'taskkill /F /PID {pid} /T')

    @property
    def consulta_menu_por_perfil(self):
        return {
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


if __name__ == '__main__':
    Interface()
