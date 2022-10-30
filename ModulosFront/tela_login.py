from tkinter import Toplevel

from ModulosFront.construtor import Construtor


class Logon:
    def login(self):
        if not self.logado and not self.root.children.get('painel_login', False):
            tela_login = Toplevel(self.root, name = 'painel_login')
            tela_login.geometry('+400+250')
            tela_login.resizable(False, False)
            tela_login.title('Login')

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

            tela_login.protocol(tela_login.protocol()[0], self.__close_event)
            self.tela_login = tela_login

    def __logar(self):
        child = self.root.children['painel_login'].children
        usuario = child['user'].get()
        senha = child['senha'].get()
        ip_servidor = child['ip_servidor'].get()
        if self.__valida_user(usuario) and self.__valida_senha(senha):
            self.logado = True
            self.user = usuario
            self.salvar_config('ip_servidor', ip_servidor)
            self.salvar_config('ultimo_user', usuario)
            for menu in self.menus_criados:
                self.menu_bar.entryconfigure(menu, state = 'normal')
            self.tela_login.destroy()

    @staticmethod
    def __valida_user(usuario):
        return usuario == 'Edimar'

    @staticmethod
    def __valida_senha(senha):
        return senha == ''

    @staticmethod
    def __close_event():
        pass

    @staticmethod
    def __validate(digito):
        if digito.isdigit() or digito == '.':
            return True
        else:
            return False
