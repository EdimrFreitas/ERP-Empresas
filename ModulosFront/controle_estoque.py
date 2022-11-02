from argparse import ArgumentParser
from tkinter import Tk
from tkcalendar import DateEntry
from os.path import abspath

from configs import Configs
from construtor import Construtor


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

    def insert_id(self, value=None, init=0):
        frame_form_child_id = self.frame_formulario.children['id']
        frame_form_child_id['state'] = 'normal'
        frame_form_child_id.insert(init, str(value))
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
            formulario_get('nome_servico'),
            self.data_criacao,
            formulario_get('quantidade'),
            formulario_get('custo'),
            formulario_get('margem_de_lucro'),
            formulario_get('categoria'),
            formulario_get('tipo'),
            formulario_get('descrição'),
        ]
        return campos_criados


class CadastroClientes(Configs, Funcoes):
    configs_path = abspath('./Configs/configs.json')

    def __init__(self):
        parser = ArgumentParser(exit_on_error = True)
        parser.add_argument('--user', default = None, required = True)
        parser.add_argument('--logado', default = None, required = True)
        args = parser.parse_args()

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

        self.novo_servico.mainloop()

    def inicia_painel(self, user):
        novo_servico = Tk()

        novo_servico.title(f'Cadastro de seviços --> {user.capitalize()}')
        novo_servico.geometry(f'{self.largura_tela(novo_servico)}x{self.altura_tela(novo_servico)}+200+100')
        novo_servico.resizable(False, False)
        novo_servico.configure(**self.root_params)

        self.novo_servico = novo_servico

    @staticmethod
    def largura_tela(novo_cliente):
        return int(novo_cliente.winfo_screenwidth() / 1.4)

    @staticmethod
    def altura_tela(novo_cliente):
        return int(novo_cliente.winfo_screenheight() / 1.4)

    def inicia_frames(self):
        frames = {
            'frame_formulario': {
                'param': dict(master = self.novo_servico, **self.frames_params),
                'place': dict(relx = 0.01, rely = 0.01, relwidth = 0.98, relheight = 0.48)
            },
            'frame_lista_produtos': {
                'param': dict(master = self.novo_servico, **self.frames_params),
                'place': dict(relx = 0.01, rely = 0.51, relwidth = 0.98, relheight = 0.48)
            }
        }
        # Cria frame dos formulários
        Construtor.frame(frames)

        # Seta marcador para as variáveis, para referenciarmos nos widgets
        self.frame_formulario = self.novo_servico.children['frame_formulario']
        self.frame_lista_produtos = self.novo_servico.children['frame_lista_produtos']

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
            'nome_servico_label': {
                'param': {'master': self.frame_formulario, **self.labels_params, 'text': 'Nome'},
                'place': {'relx': coluna2, 'rely': linha1},
            },
            'data_criacao_label': {
                'param': {'master': self.frame_formulario, **self.labels_params, 'text': 'Data de criação'},
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
            'margem_de_lucro_label': {
                'param': {'master': self.frame_formulario, **self.labels_params, 'text': 'Margem lucro'},
                'place': {'relx': coluna3, 'rely': linha2},
            },
            'categoria_label': {
                'param': {'master': self.frame_formulario, **self.labels_params, 'text': 'Categoria'},
                'place': {'relx': coluna4, 'rely': linha2},
            },
            'tipo_label': {
                'param': {'master': self.frame_formulario, **self.labels_params, 'text': 'Tipo'},
                'place': {'relx': coluna5, 'rely': linha2},
            },
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
            'nome_servico': {
                'param': {'master': self.frame_formulario, **self.entrys_params},
                'place': {
                    'relx': coluna2, 'rely': linha1 + defasagem_infos, 'relwidth': coluna4 - coluna2 + defasagem_infos
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
            'margem_de_lucro': {
                'param': {'master': self.frame_formulario, **self.entrys_params},
                'place': {'relx': coluna3, 'rely': linha2 + defasagem_infos, 'relwidth': defasagem_infos}
            },
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
                'place': {'relx': coluna4, 'rely': linha2 + defasagem_infos, 'relwidth': defasagem_infos}
            },
            'tipo': {
                'param': {'master': self.frame_formulario, 'values': self.tipos, 'state': 'readonly'},
                'place': {'relx': coluna5, 'rely': linha2 + defasagem_infos, 'relwidth': defasagem_infos},
            },
        }
        Construtor.combo_box(combo_box)

        # Cria campo calendário
        self.data_criacao = DateEntry(self.frame_formulario, **self.entrys_params, locale = "pt_br")
        self.data_criacao.place(relx = coluna5, rely = linha1 + defasagem_infos, relwidth = defasagem_infos + 0.05)

        frame_form_child_get = self.frame_formulario.children.get
        self.insert_id(value = 0)
        frame_form_child_get('nome_servico').focus_set()

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
            'pack': {'expand': True},
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
