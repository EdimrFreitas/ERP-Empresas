from tkinter import *
from tkinter.ttk import Treeview
from tkinter import TclError
from tkcalendar import DateEntry


class CadastroClientes:
    @classmethod
    def painel_cadastro_clientes(cls, sessao):
        cls.sessao = sessao
        if not sessao.logado:
            return 1
        cls.inicia_painel()

        cls.inicia_frames()
        cls.inicia_formulario()
        cls.inicia_lista_clientes()

        cls.novo_cliente.mainloop()

    @classmethod
    def inicia_painel(cls):
        novo_cliente = Tk()

        novo_cliente.title('Cadastro de clientes')
        novo_cliente.geometry(f'{cls.largura_tela(novo_cliente)}x{cls.altura_tela(novo_cliente)}+200+100')
        novo_cliente.resizable(False, False)
        novo_cliente.configure(**cls.sessao.root_params)

        novo_cliente.bind('<FocusIn>', cls.verifica)
        cls.novo_cliente = novo_cliente

    @classmethod
    def verifica(cls, _):
        try:
            cls.sessao.root.winfo_exists()
        except TclError:
            cls.novo_cliente.destroy()

    @classmethod
    def largura_tela(cls, novo_cliente):
        return int(novo_cliente.winfo_screenwidth() / 1.4)

    @classmethod
    def altura_tela(cls, novo_cliente):
        return int(novo_cliente.winfo_screenheight() / 1.4)

    @classmethod
    def inicia_frames(cls):
        # Cria frame dos formulários
        frame_formulario = Frame(**cls.sessao.frames_params, master = cls.novo_cliente)
        frame_formulario.place(relx = 0.01, rely = 0.01, relwidth = 0.98, relheight = 0.48)

        # Cria frame da lista de clientes
        frame_lista_clientes = Frame(**cls.sessao.frames_params, master = cls.novo_cliente)
        frame_lista_clientes.place(relx = 0.01, rely = 0.51, relwidth = 0.98, relheight = 0.48)

        # Seta marcador para as variáveis, para referenciarmos nos widgets
        cls.frame_formulario = frame_formulario
        cls.frame_lista_clientes = frame_lista_clientes

    @classmethod
    def inicia_formulario(cls):
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
            'Redes sociais': {
                'relx': coluna3,
                'rely': linha3
            },
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
            Label(
                master = cls.frame_formulario, **cls.sessao.labels_params, text = label
            ).place(relx = labels[label]['relx'], rely = labels[label]['rely'])

        # Define parâmetros para criar entrys
        multiplo_linha_entrys = 0.1
        width1 = 0.15
        width2 = 0.5
        width3 = 0.2
        entrys_criadas = list()

        # Cria entrys
        entrys = [
            {  # 'ID':
                'relx': coluna1,
                'rely': linha1 + multiplo_linha_entrys,
                'relwidth': width1
            },
            {  # 'Nome completo':
                'relx': coluna2,
                'rely': linha1 + multiplo_linha_entrys,
                'relwidth': width2
            },
            {  # 'CEP':
                'relx': coluna1,
                'rely': linha2 + multiplo_linha_entrys,
                'relwidth': width1
            },
            {  # 'Endereço':
                'relx': coluna2,
                'rely': linha2 + multiplo_linha_entrys,
                'relwidth': width2
            },
            {  # 'Complemento':
                'relx': coluna3,
                'rely': linha2 + multiplo_linha_entrys,
                'relwidth': width3
            },
            {  # 'Telefone':
                'relx': coluna1,
                'rely': linha3 + multiplo_linha_entrys,
                'relwidth': width1
            },
            {  # 'E-mail':
                'relx': coluna2,
                'rely': linha3 + multiplo_linha_entrys,
                'relwidth': width2
            },
            {  # 'Redes sociais':
                'relx': coluna3,
                'rely': linha3 + multiplo_linha_entrys,
                'relwidth': width3
            },
            {  # 'CPF':
                'relx': coluna1,
                'rely': linha4 + multiplo_linha_entrys,
                'relwidth': width1
            },

        ]
        for entry in entrys:
            caixa = Entry(
                master = cls.frame_formulario, **cls.sessao.entrys_params
            )
            caixa.place(**entry)
            entrys_criadas.append(caixa)

        # Cria campo calendário
        calendario1 = DateEntry(cls.frame_formulario, **cls.sessao.entrys_params, locale = "pt_br")
        calendario1.place(relx = coluna3, rely = linha1 + 0.1)
        entrys_criadas.insert(2, calendario1)

        # Dropdown do nível de permissão
        niveis_permissao = [
            'Completa',
            'Cliente',
            'Gestor',
            'Vendedor',
            'Compras',
        ]
        option = StringVar(cls.novo_cliente)
        OptionMenu(
            cls.frame_formulario, option, *niveis_permissao
        ).place(relx = coluna2, rely = linha4 + multiplo_linha_entrys - 0.02, relwidth = 0.15)
        option.set(niveis_permissao[1])
        entrys_criadas.append(option)

        # Criação dos botões
        button_width = 0.07
        Button(
            master = cls.frame_formulario, text = 'Salvar', command = lambda: cls.salvar(entrys_criadas)
        ).place(relx = coluna3, rely = linha4, relwidth = button_width, relheight = 0.18)

        Button(
            master = cls.frame_formulario, text = 'Limpar', command = lambda: cls.limpar(entrys_criadas)
        ).place(relx = coluna3 + 0.08, rely = linha4, relwidth = button_width, relheight = 0.18)

        Button(
            master = cls.frame_formulario, text = 'Buscar', command = cls.buscar
        ).place(relx = coluna3 + 0.16, rely = linha4, relwidth = button_width, relheight = 0.18)

    @classmethod
    def salvar(cls, entrys_criadas):
        infos = [entry.get() for entry in entrys_criadas]
        nome_completo = infos[1]
        numero = infos[9]
        cidade = infos[8]
        nivel = infos[10]
        cls.tabela.insert(parent = '', index = 'end', values=[nome_completo, numero, cidade, nivel])

    @classmethod
    def limpar(cls, entrys_criadas):
        for entry in entrys_criadas:
            try:
                entry.delete(0, 'end')
            except AttributeError:
                pass

    @classmethod
    def buscar(cls):
        pass

    @classmethod
    def inicia_lista_clientes(cls):
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
            master = cls.frame_lista_clientes, selectmode = 'browse',
            columns = [str(coluna) for coluna in colunas],
            show = 'tree headings',
        )
        tabela.pack(expand = True)

        cls.tabela = tabela

        tabela.column(column = '#0', width = 5)
        for coluna in colunas:
            tabela.heading(column = coluna, text = coluna)
            tabela.column(column = coluna, **colunas[coluna])


if __name__ == '__main__':
    CadastroClientes()
