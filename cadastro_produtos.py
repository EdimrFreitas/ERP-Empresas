from argparse import ArgumentParser
from tkinter import Tk, Frame, Label, Entry, OptionMenu, Button, StringVar
from tkinter.ttk import Treeview
from tkcalendar import DateEntry
from datetime import date

from configs import Configs


class CadastroClientes(Configs):
    def __init__(self):
        parser = ArgumentParser(exit_on_error = True)
        parser.add_argument('--user', default = None, required = True)
        parser.add_argument('--logado', default = None, required = True)
        args = parser.parse_args()

        self.verifica_login(args.user, args.logado)

    def verifica_login(self, user=None, logado=False):
        if not user or not logado:
            exit('Sem usuário logado')
        else:
            self.inicia_configs()
            self.painel_cadastro_produtos(user)

    def painel_cadastro_produtos(self, user):
        self.inicia_painel(user)

        self.inicia_frames()
        self.inicia_formulario()
        self.inicia_lista_clientes()

        self.novo_produto.mainloop()

    def inicia_painel(self, user):
        novo_produto = Tk()

        novo_produto.title(f'Cadastro de produtos --> {user.capitalize()}')
        novo_produto.geometry(f'{self.largura_tela(novo_produto)}x{self.altura_tela(novo_produto)}+200+100')
        novo_produto.resizable(False, False)
        novo_produto.configure(**self.root_params)

        self.novo_produto = novo_produto

    @staticmethod
    def largura_tela(novo_cliente):
        return int(novo_cliente.winfo_screenwidth() / 1.4)

    @staticmethod
    def altura_tela(novo_cliente):
        return int(novo_cliente.winfo_screenheight() / 1.4)

    def inicia_frames(self):
        tipo_lista = 'frame_lista_produtos'
        frames = {
            'frame_formulario': {
                'params': dict(master = self.novo_produto, name = 'frame_formulario', **self.frames_params),
                'grid': dict(relx = 0.01, rely = 0.01, relwidth = 0.98, relheight = 0.48)
            },
            tipo_lista: {
                'params': dict(master = self.novo_produto, name = tipo_lista, **self.frames_params),
                'grid': dict(relx = 0.01, rely = 0.51, relwidth = 0.98, relheight = 0.48)
            }
        }
        # Cria frame dos formulários
        for frame in frames:
            Frame(**frames[frame]['params']).place(**frames[frame]['grid'])

        # Seta marcador para as variáveis, para referenciarmos nos widgets
        self.frame_formulario = self.novo_produto.children.get('frame_formulario')
        self.frame_lista_clientes = self.novo_produto.children.get(tipo_lista)

    def inicia_formulario(self):
        # Parâmetros para posicionamento geral
        multiplo_linha = 0.25
        linha1 = 0.005
        linha2 = linha1 + multiplo_linha
        linha3 = linha2 + multiplo_linha
        linha4 = linha3 + multiplo_linha

        multiplo_coluna = 0.175
        coluna1 = 0.01
        coluna2 = coluna1 + multiplo_coluna
        coluna3 = coluna2 + multiplo_coluna
        coluna4 = coluna3 + multiplo_coluna
        coluna5 = coluna4 + multiplo_coluna
        coluna6 = coluna5 + multiplo_coluna

        defasagem_para_infos = 0.1

        # Cria labels
        labels = {
            'ID': {
                'relx': coluna1,
                'rely': linha1
            },
            'Nome': {
                'relx': coluna2,
                'rely': linha1
            },
            'Fabricante': {
                'relx': coluna5,
                'rely': linha1
            },
            'Quantidade': {
                'relx': coluna1,
                'rely': linha2
            },
            'Custo': {
                'relx': coluna2,
                'rely': linha2
            },
            'Cód. de barras': {
                'relx': coluna3,
                'rely': linha2
            },
            'Validade': {
                'relx': coluna4,
                'rely': linha2
            },
            'Categoria': {
                'relx': coluna5,
                'rely': linha2
            },
            'Tipo': {
                'relx': coluna6,
                'rely': linha2
            },
            # 'Impostos': {
            #     'relx': coluna3,
            #     'rely': linha3
            # },
            'Descrição': {
                'relx': coluna1,
                'rely': linha3
            },
        }
        entrys = {
            'ID': {
                'relx': coluna1,
                'rely': linha1 + defasagem_para_infos,
                'relwidth': defasagem_para_infos
            },
            'Nome': {
                'relx': coluna2,
                'rely': linha1 + defasagem_para_infos,
                'relwidth': coluna4 - coluna2 + defasagem_para_infos
            },
            'Fabricante': {
                'relx': coluna5,
                'rely': linha1 + defasagem_para_infos,
                'relwidth': coluna6 - coluna5 + defasagem_para_infos
            },
            'Quantidade': {
                'relx': coluna1,
                'rely': linha2 + defasagem_para_infos,
                'relwidth': defasagem_para_infos
            },
            'Custo': {
                'relx': coluna2,
                'rely': linha2 + defasagem_para_infos,
                'relwidth': defasagem_para_infos
            },
            'Cód de barras': {
                'relx': coluna3,
                'rely': linha2 + defasagem_para_infos,
                'relwidth': defasagem_para_infos + 0.02
            },
            # 'Impostos': {
            #     'relx': coluna3,
            #     'rely': linha3
            # },
            'Descrição': {
                'relx': coluna1,
                'rely': linha3 + defasagem_para_infos,
                'relwidth': defasagem_para_infos + coluna4 - coluna1,
                'relheight': 0.33
            },
        }
        lista_suspenca = {
            'Categoria': {
                'relx': coluna5,
                'rely': linha2 + defasagem_para_infos,
                # 'relwidth': defasagem_para_infos
            },
            'Tipo': {
                'relx': coluna6,
                'rely': linha2 + defasagem_para_infos,
                # 'relwidth': defasagem_para_infos
            },
        }

        # Cria as labels
        for label in labels:
            Label(master = self.frame_formulario, **self.labels_params, text = label).place(**labels[label])

        # Cria entrys
        entrys_criadas = list()
        for entry in entrys:
            Entry(master = self.frame_formulario, **self.entrys_params, name = entry.lower()).place(**entrys[entry])
            entrys_criadas.append(self.frame_formulario.children.get(f'{entry.lower()}'))

        # Cria campo calendário
        calendario1 = DateEntry(self.frame_formulario, **self.entrys_params, locale = "pt_br")
        calendario1.place(relx = coluna4, rely = linha2 + defasagem_para_infos, relwidth = defasagem_para_infos + 0.01)
        entrys_criadas.insert(6, calendario1)

        # Reorganizando a função TAB
        for entry in entrys_criadas:
            entry.lift()

        child_get = self.frame_formulario.children.get
        child_get('id').insert(0, '0'), child_get('id').configure(state = 'disabled')
        child_get('nome').focus_set()

        # Dropdown do nível de permissão
        niveis_permissao = ['Completa', 'Cliente', 'Gestor', 'Vendedor', 'Compras']
        option = StringVar(master = self.frame_formulario, value = niveis_permissao[0])
        for lista in lista_suspenca:
            OptionMenu(
                self.frame_formulario, option, *niveis_permissao
            ).place(
                **lista_suspenca[lista]
            )
            entrys_criadas.append(option)

        # Criação dos botões
        button_width = 0.07
        botoes = {
            'Salvar': {
                'param': dict(command = lambda: self.salvar(entrys_criadas), master = self.frame_formulario,
                              text = 'Salvar'),
                'place': dict(relx = 0.75, rely = linha4, relwidth = button_width, relheight = 0.18)
            },
            'Limpar': {
                'param': dict(command = lambda: self.limpar(entrys_criadas), master = self.frame_formulario,
                              text = 'Limpar'),
                'place': dict(relx = 0.75 + 0.08, rely = linha4, relwidth = button_width, relheight = 0.18)
            },
            'Buscar': {
                'param': dict(command = lambda: self.buscar(entrys_criadas), master = self.frame_formulario,
                              text = 'Buscar'),
                'place': dict(relx = 0.075 + 0.16, rely = linha4, relwidth = button_width, relheight = 0.18)
            }
        }
        for botao in botoes:
            Button(**botoes[botao]['param'], name = botao.lower()).place(**botoes[botao]['place'])

    def salvar(self, entrys_criadas):
        infos = [entry.get() for entry in entrys_criadas]
        nome_completo = infos[1]
        numero = infos[9]
        cidade = infos[8]
        nivel = infos[10]
        self.tabela.insert(parent = '', index = 'end', values = [nome_completo, numero, cidade, nivel])

    @staticmethod
    def limpar(entrys_criadas):
        for entry in entrys_criadas:
            try:
                entry.delete(0, 'end')
            except AttributeError:
                pass

    def buscar(self, entrys_criadas):
        pass

    def inicia_lista_clientes(self):
        colunas = {
            'Nome completo': {
                'width': 600,
                'anchor': 'w'
            },
            'Número': {
                'width': 100,
                'anchor': 'center'
            },
            'Cidade': {
                'width': 100,
                'anchor': 'center'
            },
            'Permissão': {
                'width': 100,
                'anchor': 'center'
            }
        }
        tabela = Treeview(master = self.frame_lista_clientes, selectmode = 'browse',
                          columns = [str(coluna) for coluna in colunas], show = 'tree headings'
                          )
        tabela.pack(expand = True)

        self.tabela = tabela

        tabela.column(column = '#0', width = 5)
        for coluna in colunas:
            tabela.heading(column = coluna, text = coluna)
            tabela.column(column = coluna, **colunas[coluna])


if __name__ == '__main__':
    CadastroClientes()
