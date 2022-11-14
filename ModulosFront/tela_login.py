from tkinter import Toplevel

from ModulosFront.construtor import Construtor


class Logon:
    def __init__(self):
        tela_login = Toplevel(self.root, name = 'painel_login')
        tela_login.geometry('+400+250')
        tela_login.resizable(False, False)
        tela_login.title('Login')
        tela_login.protocol(tela_login.protocol()[0], self.__close_event)

        labels = {
            'usuario': {
                'param': {'master': tela_login, 'text': 'Usuário', 'font': 'arial 9 bold'},
                'grid': {'row': 1, 'column': 1, 'padx': 5, 'pady': 5, 'sticky': 'e'}
            },
            'senha': {
                'param': {'master': tela_login, 'text': 'Senha', 'font': 'arial 9 bold'},
                'grid': {'row': 2, 'column': 1, 'padx': 5, 'pady': 5, 'sticky': 'e'}
            },
            'ip_servidor': {
                'param': {'master': tela_login, 'text': 'IP do servidor', 'font': 'arial 9 bold'},
                'grid': {'row': 3, 'column': 1, 'padx': 5, 'pady': 5, 'sticky': 'e'}
            }
        }
        Construtor.label(labels)

        entrys = {
            'user': {
                'param': {'master': tela_login, 'name': 'user'},
                'grid': {'row': 1, 'column': 2, 'padx': 5, 'pady': 5}
            },
            'senha': {
                'param': {'master': tela_login, 'name': 'senha', 'show': '*'},
                'grid': {'row': 2, 'column': 2, 'padx': 5, 'pady': 5}
            },
            'ip_servidor': {
                'param': {'master': tela_login, 'name': 'ip_servidor'},
                'grid': {'row': 3, 'column': 2, 'padx': 5, 'pady': 5}
            }
        }
        Construtor.entry(entrys)

        buttons = {
            'bt_login': {
                'param': dict(master = tela_login, text = 'Login', command = self.__logar),
                'grid': dict(sticky = 'NS' + 'EW', row = 4, column = 1, columnspan = 2, padx = 5, pady = 5)
            }
        }
        Construtor.button(buttons)

        vcmd = (tela_login.register(self.__validate), '%S')

        child = tela_login.children
        child['user'].focus_set()
        child['user'].insert(0, self.ultimo_user)
        child['user'].bind('<Return>', lambda e: child['senha'].focus_set(), add = '+')

        child['senha'].bind('<Return>', lambda e: self.__logar())

        child['ip_servidor'].insert(0, self.ip_servidor)
        child['ip_servidor'].bind('<Return>', lambda e: self.__logar())
        child['ip_servidor'].configure(dict(validate = 'key', validatecommand = vcmd))

        self.tela_login = tela_login

    def __logar(self):
        if self.__authentica():
            self.logado = True
            self.user = self.__usuario
            self.password = self.__senha

            self.inicia_menu()

            self.tela_login.destroy()
        else:
            Construtor.show_info(titulo = 'Login mal sucedido', mensagem = 'Informações de autenticação incorretos')
            Logon.__init__(self)

    def __authentica(self):
        return self.__usuario == 'Edimar' and self.__senha == '12345'

    @property
    def __usuario(self):
        return self.root.children['painel_login'].children['user'].get()

    @property
    def __senha(self):
        return self.root.children['painel_login'].children['senha'].get()

    @property
    def __ip_servidor(self):
        return self.root.children['painel_login'].children['ip_servidor'].get()

    @staticmethod
    def __validate(digito):
        if digito.isdigit() or digito == '.':
            return True
        else:
            return False

    @staticmethod
    def __close_event():
        pass
