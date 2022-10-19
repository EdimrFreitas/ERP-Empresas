from tkinter import Toplevel, Label, Entry, Button, StringVar


class Logon:
    def login(self):
        if not self.logado and not self.root.children.get('painel_login', False):
            tela_login = Toplevel(self.root, name = 'painel_login')
            tela_login.geometry('+400+250')
            tela_login.resizable(False, False)
            tela_login.title('Login')

            Label(tela_login, text = 'Usuário').grid(row = 1, column = 1, padx = 5, pady = 5)
            Label(tela_login, text = 'senha').grid(row = 2, column = 1, padx = 5, pady = 5)
            Label(tela_login, text = 'IP do servidor').grid(row = 3, column = 1, padx = 5, pady = 5)

            usuario = StringVar(master = tela_login, value = self.ultimo_user)
            senha = StringVar(master = tela_login, value = '')
            ip_servidor = StringVar(master = tela_login, value = self.ip_servidor)

            entrys = {
                'user': {
                    'param': {'master': tela_login, 'textvariable': usuario, 'name': 'user'},
                    'grid': {'row': 1, 'column': 2, 'padx': 5, 'pady': 5}
                },
                'senha': {
                    'param': {'master': tela_login, 'textvariable': senha, 'name': 'senha'},
                    'grid': {'row': 2, 'column': 2, 'padx': 5, 'pady': 5}
                },
                'ip_servidor': {
                    'param': {'master': tela_login, 'textvariable': ip_servidor, 'name': 'ip_servidor'},
                    'grid': {'row': 3, 'column': 2, 'padx': 5, 'pady': 5}
                }
            }
            for entry in entrys:
                Entry(**entrys[entry]['param']).grid(**entrys[entry]['grid'])

            btn = Button(tela_login, text = 'Login',
                         command = lambda: self.logar(usuario.get(), senha.get(), ip_servidor.get())
                         )
            btn.grid(sticky = 'NS' + 'EW', row = 4, column = 1, columnspan = 2, padx = 5, pady = 5)

            tela_login.winfo_children()[3].focus_set()
            child = tela_login.children
            child.get('user').bind('<Return>', lambda e: tela_login.children.get('senha').focus_set())
            child.get('senha').bind('<Return>', lambda e: self.logar(usuario.get(), senha.get(), ip_servidor.get()))
            self.tela_login = tela_login

    def logar(self, usuario=None, senha=None, ip_servidor=None):
        if self.valida_user(usuario) and self.valida_senha(senha):
            self.logado = True
            self.user = usuario
            self.salvar_config('ip_servidor', ip_servidor)
            self.salvar_config('ultimo_user', usuario)
            for menu in self.menus_criados:
                self.menu_bar.entryconfigure(menu, state = 'normal')
            self.tela_login.destroy()

    @staticmethod
    def valida_user(usuario):
        return usuario.lower() == 'edimar'

    @staticmethod
    def valida_senha(senha):
        return senha == ''
