from tkinter import Toplevel, BooleanVar
from threading import Thread

from ModulosFront.construtor import Construtor
from ModulosFront.conector import ConectorBD


class Logon:
    def __init__(self):
        tela_login = Toplevel(self.root, name = 'painel_login')
        tela_login.geometry('+400+250')
        tela_login.resizable(False, False)
        tela_login.title('Login')
        tela_login.protocol(tela_login.protocol()[0], self.__close_event)
        fonte = 'arial 9 bold'
        padding = {'padx': 5, 'pady': 5}

        labels = {
            'usuario': {
                'param': {'master': tela_login, 'text': 'Usuário', 'font': fonte},
                'grid': {'row': 1, 'column': 1, 'sticky': 'e', **padding}
            },
            'senha': {
                'param': {'master': tela_login, 'text': 'Senha', 'font': fonte},
                'grid': {'row': 2, 'column': 1, **padding, 'sticky': 'e'}
            },
            'ip_servidor': {
                'param': {'master': tela_login, 'text': 'IP do servidor', 'font': fonte},
                'grid': {'row': 3, 'column': 1, **padding, 'sticky': 'e'}
            }
        }
        Construtor.label(labels)

        entrys = {
            'user': {
                'param': {'master': tela_login, 'name': 'user'},
                'grid': {'row': 1, 'column': 2, **padding}
            },
            'senha': {
                'param': {'master': tela_login, 'name': 'senha', 'show': '*'},
                'grid': {'row': 2, 'column': 2, **padding}
            },
            'ip_servidor': {
                'param': {'master': tela_login, 'name': 'ip_servidor'},
                'grid': {'row': 3, 'column': 2, **padding}
            }
        }
        Construtor.entry(entrys)

        self.__salva_user = BooleanVar()

        check_buttons = {
            'salva_user': {
                'param': {'master': tela_login, 'text': 'Salvar usuário', 'variable': self.__salva_user},
                'grid': {'row': 1, 'column': 3, **padding}
            }
        }
        Construtor.check_button(check_buttons)

        buttons = {
            'bt_login': {
                'param': dict(master = tela_login, text = 'Login', command = self.__logar),
                'grid': dict(sticky = 'NS' + 'EW', row = 4, column = 1, columnspan = 2, padx = 5, pady = 5)
            }
        }
        Construtor.button(buttons)

        child = tela_login.children
        child['user'].focus_set()
        child['user'].insert(0, self.ultimo_user)
        child['user'].bind('<Return>', lambda e: child['senha'].focus_set(), add = '+')

        child['salva_user'].bind('<Return>', lambda e: child['salva_user'].toggle())

        child['senha'].bind('<Return>', lambda e: self.__logar())

        vcmd = (tela_login.register(self.__validate), '%S')
        child['ip_servidor'].insert(0, self.ip_servidor)
        child['ip_servidor'].bind('<Return>', lambda e: self.__logar())
        child['ip_servidor'].configure(dict(validate = 'key', validatecommand = vcmd))

        child['bt_login'].bind('<Return>', lambda e: self.__logar())

        self.tela_login = tela_login

    # Login

    def __logar(self):
        usuario = self.__usuario
        senha = self.__senha
        servidor = self.__ip_servidor

        if self.__authentica(usuario, senha, servidor):
            self.user = self.__conexao.usuario.usuario
            self.password = self.__conexao.usuario.senha
            self.perfil = self.__conexao.perfil.perfil
            self.logado = True
            self.permissoes = self.__conexao.permissoes

            if self.__salvar_user:
                self.salva_ultimo_login()

            self.inicia_menu()

            self.tela_login.destroy()
        else:
            Construtor.show_info(titulo = 'Login mal sucedido', mensagem = 'Informações de autenticação incorretos')
            Logon.__init__(self)

    def __authentica(self, usuario, senha, servidor):
        conexao = ConectorBD(ip=servidor, usuario=usuario, senha=senha)
        self.__conexao = conexao
        if conexao.usuario.status == 'Conectado':
            return True
        else:
            return False

    # Propertys

    @property
    def __usuario(self):
        return self.root.children['painel_login'].children['user'].get()

    @property
    def __senha(self):
        return self.root.children['painel_login'].children['senha'].get()

    @property
    def __ip_servidor(self):
        return str(self.root.children['painel_login'].children['ip_servidor'].get())

    @property
    def __salvar_user(self):
        return self.__salva_user.get()

    # Staticmethods

    @staticmethod
    def __validate(digito):
        if digito.isdigit() or digito == '.':
            return True
        else:
            return False

    @staticmethod
    def __close_event():
        pass

    def salva_ultimo_login(self):
        pass
