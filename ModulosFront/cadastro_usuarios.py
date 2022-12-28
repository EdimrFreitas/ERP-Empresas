from tkinter import Tk, Label, Entry, Button
from tkinter.ttk import Treeview
from tkcalendar import DateEntry
from os.path import abspath

from configs import Configs
from construtor import Construtor
from inicializador import Argumentos


class Funcoes:
    @staticmethod
    def largura_tela(novo_cliente):
        return int(novo_cliente.winfo_screenwidth() / 1.4)

    @staticmethod
    def altura_tela(novo_cliente):
        return int(novo_cliente.winfo_screenheight() / 1.4)

    def salvar(self, entrys_criadas):
        infos = [entry.get() for entry in entrys_criadas]
        nome_completo = infos[1]
        numero = infos[6]
        cidade = infos[4]
        nivel = infos[9]
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

    def insert_id(self, row=0, value=None):
        frame_form_child_id = self.frame_formulario.children['id_entry']
        frame_form_child_id['state'] = 'normal'
        frame_form_child_id.insert(row, str(value))
        frame_form_child_id['state'] = 'readonly'


class CadastroClientes(Configs, Funcoes):
    configs_path = abspath('./Configs/configs.json')

    def __init__(self):
        args = Argumentos.argumentos()
        Configs.__init__(self, self.configs_path)

        self.verifica_login(args.user, args.logado)

    def verifica_login(self, user=None, logado=False):
        if not user or not logado:
            exit('Sem usuário logado')
        else:
            self.painel_cadastro_clientes(user)

    def painel_cadastro_clientes(self, user):
        self.inicia_painel(user)

        self.inicia_frames()
        self.inicia_formulario()
        self.inicia_lista_clientes()

        self.novo_cliente.mainloop()

    def inicia_painel(self, user):
        novo_cliente = Tk()

        novo_cliente.title(f'Cadastro de clientes --> {user.capitalize()}')
        novo_cliente.geometry(f'{self.largura_tela(novo_cliente)}x{self.altura_tela(novo_cliente)}+200+100')
        novo_cliente.resizable(False, False)
        novo_cliente.configure(**self.root_params)

        self.novo_cliente = novo_cliente

    def inicia_frames(self):
        frames = {
            'frame_formulario': {
                'param': dict(master = self.novo_cliente, name = 'frame_formulario'),
                'place': dict(relx = 0.01, rely = 0.01, relwidth = 0.98, relheight = 0.48)
            },
            'frame_lista_clientes': {
                'param': dict(master = self.novo_cliente, name = 'frame_lista_clientes'),
                'place': dict(relx = 0.01, rely = 0.51, relwidth = 0.98, relheight = 0.48)
            }
        }
        # Cria frame dos formulários
        Construtor.frame(frames)

        # Seta marcador para as variáveis, para referenciarmos nos widgets
        self.frame_formulario = self.novo_cliente.children.get('frame_formulario')
        self.frame_lista_clientes = self.novo_cliente.children.get('frame_lista_clientes')

    def inicia_formulario(self):
        # Parâmetros para posicionamento geral
        linha1 = 0.005
        multiplo_linha = 0.25
        coluna1 = 0.02

        linha2 = linha1 + multiplo_linha
        coluna2 = coluna1 + 0.18

        linha3 = linha2 + multiplo_linha
        coluna3 = coluna2 + 0.55

        linha4 = linha3 + multiplo_linha

        # Cria labels
        labels = {
            'ID': {
                'relx': coluna1,
                'rely': linha1
            },
            'Nome completo': {
                'relx': coluna2,
                'rely': linha1
            },
            'Data de nascimento': {
                'relx': coluna3,
                'rely': linha1
            },
            'CEP': {
                'relx': coluna1,
                'rely': linha2
            },
            'Endereço': {
                'relx': coluna2,
                'rely': linha2
            },
            'Complemento': {
                'relx': coluna3,
                'rely': linha2
            },
            'Telefone': {
                'relx': coluna1,
                'rely': linha3
            },
            'E-mail': {
                'relx': coluna2,
                'rely': linha3
            },
            # 'Redes sociais': {
            #     'relx': coluna3,
            #     'rely': linha3
            # },
            'CPF': {
                'relx': coluna1,
                'rely': linha4
            },
            'Nível de permissão': {
                'relx': coluna2,
                'rely': linha4
            },
        }
        for label in labels:
            Label(master = self.frame_formulario, **self.labels_params, text = label).place(**labels[label])

        # Define parâmetros para criar entrys
        multiplo_linha_entrys = 0.1
        width1 = 0.15
        width2 = 0.5
        width3 = 0.2
        entrys_criadas = list()

        # Cria entrys
        entrys = {
            'ID_entry': {
                'relx': coluna1,
                'rely': linha1 + multiplo_linha_entrys,
                'relwidth': width1
            },
            'Nome completo_entry': {
                'relx': coluna2,
                'rely': linha1 + multiplo_linha_entrys,
                'relwidth': width2
            },
            'CEP_entry': {  #
                'relx': coluna1,
                'rely': linha2 + multiplo_linha_entrys,
                'relwidth': width1
            },
            'Endereço_entry': {  #
                'relx': coluna2,
                'rely': linha2 + multiplo_linha_entrys,
                'relwidth': width2
            },
            'Complemento_entry': {  #
                'relx': coluna3,
                'rely': linha2 + multiplo_linha_entrys,
                'relwidth': width3
            },
            'Telefone_entry': {  #
                'relx': coluna1,
                'rely': linha3 + multiplo_linha_entrys,
                'relwidth': width1
            },
            'E-mail_entry': {  #
                'relx': coluna2,
                'rely': linha3 + multiplo_linha_entrys,
                'relwidth': width2
            },
            # 'Redes sociais':{
            #     'relx': coluna3,
            #     'rely': linha3 + multiplo_linha_entrys,
            #     'relwidth': width3
            # },
            'CPF_entry': {  #
                'relx': coluna1,
                'rely': linha4 + multiplo_linha_entrys,
                'relwidth': width1
            },
        }
        for entry in entrys:
            Entry(master = self.frame_formulario, **self.entrys_params, name = entry.lower()).place(**entrys[entry])
            entrys_criadas.append(self.frame_formulario.children.get(f'{entry.lower()}'))

        # Cria campo calendário
        calendario1 = DateEntry(self.frame_formulario, **self.entrys_params, locale = "pt_br")
        calendario1.place(relx = coluna3, rely = linha1 + 0.1)
        entrys_criadas.insert(2, calendario1)

        # Reorganizando a função TAB
        for entry in entrys_criadas:
            entry.lift()

        child_get = self.frame_formulario.children.get
        self.insert_id(value = 0)
        child_get('nome completo_entry').focus_set()

        # Dropdown do nível de permissão
        niveis_permissao = ['Total', 'Gestor', 'Vendedor', 'Comprador']
        niveis_permissao.sort()
        combos = {
            'nivel_permissao': {
                'param': {'master': self.frame_formulario, 'values': niveis_permissao, 'state': 'readonly'},
                'place': dict(relx = coluna2, rely = linha4 + multiplo_linha_entrys - 0.02, relwidth = 0.15)
            }
        }
        Construtor.combo_box(combos)

        child_permissao = child_get('nivel_permissao')
        child_permissao.current(0)
        entrys_criadas.append(child_permissao)
        child_permissao.bind('<<ComboboxSelected>>', lambda e: self.verifica_tipo_cadastro())

        # Criação dos botões
        button_width = 0.07
        botoes = {
            'Salvar': {
                'param': dict(command = lambda: self.salvar(entrys_criadas), master = self.frame_formulario,
                              text = 'Salvar'),
                'place': dict(relx = coluna3, rely = linha4, relwidth = button_width, relheight = 0.18)
            },
            'Limpar': {
                'param': dict(command = lambda: self.limpar(entrys_criadas), master = self.frame_formulario,
                              text = 'Limpar'),
                'place': dict(relx = coluna3 + 0.08, rely = linha4, relwidth = button_width, relheight = 0.18)
            },
            'Buscar': {
                'param': dict(command = lambda: self.buscar(entrys_criadas), master = self.frame_formulario,
                              text = 'Buscar'),
                'place': dict(relx = coluna3 + 0.16, rely = linha4, relwidth = button_width, relheight = 0.18)
            }
        }
        for botao in botoes:
            Button(**botoes[botao]['param'], name = botao.lower()).place(**botoes[botao]['place'])

    def verifica_tipo_cadastro(self):
        child_get = self.frame_formulario.children.get
        permissao = child_get('nivel_permissao').get()
        if permissao != 'Cliente' and not child_get('senha', False):
            campo_senha = {
                'senha': {
                    'param': {'master': self.frame_formulario, **self.entrys_params},
                    'place': {'relx': 0.55, 'rely': 0.755}
                }
            }
            Construtor.entry(campo_senha)

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
        tabela = Treeview(
            master = self.frame_lista_clientes, selectmode = 'browse',
            columns = [str(coluna) for coluna in colunas], show = 'tree headings'
        )
        tabela.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)

        self.tabela = tabela

        tabela.column(column = '#0', width = 5)
        for coluna in colunas:
            tabela.heading(column = coluna, text = coluna)
            tabela.column(column = coluna, **colunas[coluna])


if __name__ == '__main__':
    CadastroClientes()
