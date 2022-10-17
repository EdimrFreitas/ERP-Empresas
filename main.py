from tkinter import *

from configuracoes import Configs
from tela_login import Logon
from cadastros import CadastroClientes


class Menus:
    def cadastro_clientes(self):
        CadastroClientes.painel_cadastro_clientes(sessao = self)

    def cadastro_produtos(self):
        pass

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


class Interface(Menus, Configs, Logon):
    logado = False
    menus_criados = list()

    def __init__(self):
        self.inicia_configs()
        self.inicia_root()
        self.inicia_menu()
        self.root.mainloop()

    # Inicia a tela com nome da empresa
    def inicia_root(self):
        root = Tk()
        root.title(self.nome_da_empresa)
        largura_tela = int(root.winfo_screenwidth() / 1.2)
        altura_tela = int(root.winfo_screenheight() / 1.2)
        root.geometry(f'{largura_tela}x{altura_tela}+50+30')
        root.configure(**self.root_params)

        root.bind('<FocusIn>', lambda e: self.login(e))

        self.root = root

    # -------------------------------------------------------------------------------------------------------------------------------------------#
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

        for menu_superior in menus.keys():
            novo_menu = Menu(master = menu_bar, tearoff = 0)
            menu_bar.add_cascade(label = menu_superior, menu = novo_menu, state = 'disabled')
            self.menus_criados.append(menu_superior)

            for menu_inferior, comando in menus[menu_superior]:
                novo_menu.add_command(label = menu_inferior, command = comando)


        self.root.config(menu = menu_bar)
        self.menu_bar = menu_bar



if __name__ == '__main__':
    Interface()
