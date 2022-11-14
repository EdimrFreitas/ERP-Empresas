from argparse import ArgumentParser
from tkinter import Tk
from tkcalendar import DateEntry
from os.path import abspath

from configs import Configs
from construtor import Construtor
from inicializador import Argumentos

class Funcoes:
    @staticmethod
    def verifica_login(user=None, logado=False):
        if not user or not logado:
            return False
        else:
            return True

    def salvar(self):
        infos = [entry.get() for entry in self.campos_criados]

    def limpar(self):
        formulario_get = self.frame_formulario.children.get
        formulario_get('id').config()
        formulario_get('nome').delete(0, 'end')
        formulario_get('fabricante').delete(0, 'end')
        formulario_get('quantidade').delete(0, 'end')
        formulario_get('custo').delete(0, 'end')
        formulario_get('cod_barras').delete(0, 'end')
        formulario_get('descrição').delete(0, 'end')

    def buscar(self):
        pass

    def insert_id(self, row=0, value=None):
        frame_form_child_id = self.frame_formulario.children['id']
        frame_form_child_id['state'] = 'normal'
        frame_form_child_id.insert(row, str(value))
        frame_form_child_id['state'] = 'readonly'

    @property
    def categorias(self):
        return ['Completa', 'Cliente', 'Gestor', 'Vendedor', 'Compras']

    @property
    def tipos(self):
        return ['Completa', 'Cliente', 'Gestor', 'Vendedor', 'Compras']

    @property
    def campos_criados(self):
        formulario_get = self.frame_formulario.children.get
        campos_criados = [
            formulario_get('id'),
            formulario_get('nome'),
            formulario_get('fabricante'),
            formulario_get('quantidade'),
            formulario_get('custo'),
            formulario_get('cod_barras'),
            self.calendario1,
            formulario_get('categoria'),
            formulario_get('tipo'),
            formulario_get('descrição'),
        ]
        return campos_criados


class CadastroClientes(Configs, Funcoes):
    configs_path = abspath('./Configs/configs.json')

    def __init__(self):
        args = Argumentos.argumentos()

        if self.verifica_login(args.user, args.logado):
            Configs.__init__(self, self.configs_path)
            self.painel_cadastro_produtos(args.user)
        else:
            exit('Sem usuário logado')

    def painel_cadastro_produtos(self, user):
        self.inicia_painel(user)

        self.inicia_frames()
        self.inicia_formulario()
        self.inicia_lista_produtos()

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
        notebooks = {
            'notebook': {
                'param': {'master': self.novo_produto},
                'place': {'relx': 0.01, 'rely': 0.01, 'relwidth': 0.98, 'relheight': 0.48},
            }
        }
        Construtor.notebook(notebooks)

        notebook = self.novo_produto.children['notebook']

        frames = {
            'frame_formulario': {
                'param': {'master': notebook, **self.frames_params},
                'place': {'relx': 0.01, 'rely': 0.01, 'relwidth': 0.98, 'relheight': 0.48}
            },
            'frame_configs': {
                'param': {'master': notebook, **self.frames_params},
                'place': {'relx': 0.01, 'rely': 0.01, 'relwidth': 0.98, 'relheight': 0.48}
            },
            'frame_lista_produtos': {
                'param': dict(master = self.novo_produto, **self.frames_params),
                'place': dict(relx = 0.01, rely = 0.51, relwidth = 0.98, relheight = 0.48)
            }
        }
        # Cria frame dos formulários
        Construtor.frame(frames)

        abas = {
            'notebook': notebook,
            'abas': {
                'Cadastro': {'child': notebook.children['frame_formulario']},
                'Controle de estoque': {'child': notebook.children['frame_configs']},
            }
        }
        Construtor.add_abas(abas)

        # Seta marcador para as variáveis, para referenciarmos nos widgets
        self.frame_formulario = notebook.children['frame_formulario']
        self.frame_lista_produtos = self.novo_produto.children['frame_lista_produtos']

    def inicia_formulario(self):
        # Parâmetros para posicionamento geral
        multiplo_linha = 0.25
        linha1 = 0.005
        linha2 = linha1 + multiplo_linha
        linha3 = linha2 + multiplo_linha
        linha4 = linha3 + multiplo_linha

        multiplo_coluna = 0.17
        coluna1 = 0.01
        coluna2 = coluna1 + multiplo_coluna
        coluna3 = coluna2 + multiplo_coluna
        coluna4 = coluna3 + multiplo_coluna
        coluna5 = coluna4 + multiplo_coluna
        coluna6 = coluna5 + multiplo_coluna

        defasagem_infos = 0.1

        # Cria labels
        labels = {
            'id_label': {
                'param': {'master': self.frame_formulario, **self.labels_params, 'text': 'ID'},
                'place': {'relx': coluna1, 'rely': linha1}
            },
            'nome_label': {
                'param': {'master': self.frame_formulario, **self.labels_params, 'text': 'Nome'},
                'place': {'relx': coluna2, 'rely': linha1},
            },
            'fabricante_label': {
                'param': {'master': self.frame_formulario, **self.labels_params, 'text': 'Fabricante'},
                'place': {'relx': coluna5, 'rely': linha1},
            },
            'quantidade_label': {
                'param': {'master': self.frame_formulario, **self.labels_params, 'text': 'Quantidade'},
                'place': {'relx': coluna1, 'rely': linha2},
            },
            'custo_label': {
                'param': {'master': self.frame_formulario, **self.labels_params, 'text': 'Custo'},
                'place': {'relx': coluna2, 'rely': linha2},
            },
            'cod_de_barras_label': {
                'param': {'master': self.frame_formulario, **self.labels_params, 'text': 'Cód. de barras'},
                'place': {'relx': coluna3, 'rely': linha2},
            },
            'validade_label': {
                'param': {'master': self.frame_formulario, **self.labels_params, 'text': 'Validade'},
                'place': {'relx': coluna4, 'rely': linha2},
            },
            'categoria_label': {
                'param': {'master': self.frame_formulario, **self.labels_params, 'text': 'Categoria'},
                'place': {'relx': coluna5, 'rely': linha2},
            },
            'tipo_label': {
                'param': {'master': self.frame_formulario, **self.labels_params, 'text': 'Tipo'},
                'place': {'relx': coluna6, 'rely': linha2},
            },
            # 'Impostos_label': {
            #                 'param': {'master': self.frame_formulario, **self.labels_params, 'text': 'Impostos'},
            #                 'place': {'relx': coluna3, 'rely': linha3},
            # },
            'descrição_label': {
                'param': {'master': self.frame_formulario, **self.labels_params, 'text': 'Descrição'},
                'place': {'relx': coluna1, 'rely': linha3},
            },
        }
        # Cria as labels
        Construtor.label(labels)

        entrys = {
            'id': {
                'param': {'master': self.frame_formulario, **self.entrys_params},
                'place': {'relx': coluna1, 'rely': linha1 + defasagem_infos, 'relwidth': defasagem_infos}
            },
            'nome': {
                'param': {'master': self.frame_formulario, **self.entrys_params},
                'place': {
                    'relx': coluna2, 'rely': linha1 + defasagem_infos,
                    'relwidth': coluna4 - coluna2 + defasagem_infos
                }
            },
            'fabricante': {
                'param': {'master': self.frame_formulario, **self.entrys_params},
                'place': {
                    'relx': coluna5, 'rely': linha1 + defasagem_infos,
                    'relwidth': coluna6 - coluna5 + defasagem_infos
                }
            },
            'quantidade': {
                'param': {'master': self.frame_formulario, **self.entrys_params},
                'place': {'relx': coluna1, 'rely': linha2 + defasagem_infos, 'relwidth': defasagem_infos}
            },
            'custo': {
                'param': {'master': self.frame_formulario, **self.entrys_params},
                'place': {'relx': coluna2, 'rely': linha2 + defasagem_infos, 'relwidth': defasagem_infos}
            },
            'cod_barras': {
                'param': {'master': self.frame_formulario, **self.entrys_params},
                'place': {
                    'relx': coluna3, 'rely': linha2 + defasagem_infos, 'relwidth': defasagem_infos + 0.02
                }
            },
            # 'Impostos': {
            #     'param': 'master': self.frame_formulario, **self.entrys_params,
            #     'place': {'relx': coluna3, 'rely': linha3}
            # }
            # 
        }
        # Cria entrys
        Construtor.entry(entrys)

        texts = {
            'descrição': {
                'param': {'master': self.frame_formulario, **self.entrys_params},
                'place': {
                    'relx': coluna1, 'rely': linha3 + defasagem_infos,
                    'relwidth': defasagem_infos + coluna4 - coluna1, 'relheight': 0.33
                }
            },
        }
        # Cria Text
        Construtor.text(texts)

        # Crias as combo box
        combo_box = {
            'categoria': {
                'param': {'master': self.frame_formulario, 'values': self.categorias, 'state': 'readonly'},
                'place': {'relx': coluna5, 'rely': linha2 + defasagem_infos, 'relwidth': defasagem_infos}
            },
            'tipo': {
                'param': {'master': self.frame_formulario, 'values': self.tipos, 'state': 'readonly'},
                'place': {'relx': coluna6, 'rely': linha2 + defasagem_infos, 'relwidth': defasagem_infos},
            },
        }
        Construtor.combo_box(combo_box)

        # Cria campo calendário
        self.calendario1 = DateEntry(self.frame_formulario, **self.entrys_params, locale = "pt_br")
        self.calendario1.place(relx = coluna4, rely = linha2 + defasagem_infos, relwidth = defasagem_infos + 0.01)

        self.insert_id(value = '0')
        self.frame_formulario.children.get('nome').focus_set()

        # Reorganizando a função TAB
        for campo in self.campos_criados:
            campo.lift()

        # Criação dos botões
        button_width = 0.07
        botoes = {
            'salvar': {
                'param': dict(command = self.salvar, master = self.frame_formulario, text = 'Salvar'),
                'place': dict(relx = coluna5, rely = linha4, relwidth = button_width, relheight = 0.18)
            },
            'limpar': {
                'param': dict(command = self.limpar, master = self.frame_formulario,
                              text = 'Limpar'),
                'place': dict(relx = coluna5 + 0.08, rely = linha4, relwidth = button_width, relheight = 0.18)
            },
            'buscar': {
                'param': dict(command = self.buscar, master = self.frame_formulario,
                              text = 'Buscar'),
                'place': dict(relx = coluna5 + 0.16, rely = linha4, relwidth = button_width, relheight = 0.18)
            }
        }
        Construtor.button(botoes)

    def inicia_lista_produtos(self):
        tree_produtos = {
            'param': {
                'master': self.frame_lista_produtos,
                'name': 'tree_produtos',
                'show': 'headings'
            },
            'place': {'relx': 0, 'rely': 0, 'relwidth': 1, 'relheight': 1},
            'colunas': {
                'ID': {
                    'heading': {'anchor': 'w'},
                    'column': {'anchor': 'w', 'minwidth': 25, 'stretch': True, 'width': 50},
                },
                'Nome': {
                    'heading': {'anchor': 'w'},
                    'column': {'anchor': 'w', 'minwidth': 25, 'stretch': True, 'width': 150},
                },
                'Fabricante': {
                    'heading': {'anchor': 'w'},
                    'column': {'anchor': 'w', 'minwidth': 25, 'stretch': True, 'width': 150},
                },
                'Quant.': {
                    'heading': {'anchor': 'center'},
                    'column': {'anchor': 'w', 'minwidth': 25, 'stretch': True, 'width': 100},
                },
                'Custo': {
                    'heading': {'anchor': 'center'},
                    'column': {'anchor': 'w', 'minwidth': 25, 'stretch': True, 'width': 100},
                },
                'Valor': {
                    'heading': {'anchor': 'center'},
                    'column': {'anchor': 'w', 'minwidth': 25, 'stretch': True, 'width': 100},
                },
                'Validade': {
                    'heading': {'anchor': 'w'},
                    'column': {'anchor': 'w', 'minwidth': 25, 'stretch': True, 'width': 100},
                },
                'Categoria': {
                    'heading': {'anchor': 'w'},
                    'column': {'anchor': 'w', 'minwidth': 25, 'stretch': True, 'width': 100},
                },
                'Tipo': {
                    'heading': {'anchor': 'w'},
                    'column': {'anchor': 'w', 'minwidth': 25, 'stretch': True, 'width': 100},
                },
            }
        }
        Construtor.tree_view(tree_produtos)

        tabela = self.frame_lista_produtos.children['tree_produtos']
        tabela.column('#0', width = False)


if __name__ == '__main__':
    CadastroClientes()
