from tkinter import Toplevel, Label, Entry, Button


class Logon:
    def login(self, _):
        if not self.logado and not self.root.children.get('painel_login', False):
            tela_login = Toplevel(self.root, name = 'painel_login')
            tela_login.geometry('300x100+400+250')
            tela_login.resizable(False, False)
            tela_login.title('Login')

            Label(tela_login, text = 'Usuário').grid(row = 1, column = 1, padx = 5, pady = 5)
            Label(tela_login, text = 'senha').grid(row = 2, column = 1, padx = 5, pady = 5)

            usuario = Entry(tela_login)
            usuario.grid(row = 1, column = 2, padx = 5, pady = 5)

            senha = Entry(tela_login, show = '*')
            senha.grid(row = 2, column = 2, padx = 5, pady = 5)

            Button(
                tela_login, text = 'Login',
                command = lambda: self.logar(usuario.get(), senha.get())
            ).grid(sticky = 'NS' + 'EW', row = 3, column = 1, columnspan = 2, padx = 5, pady = 5)

            self.tela_login = tela_login

    def logar(self, usuario, senha):
        if usuario == '' and senha == '':
            self.logado = True
            for menu in self.menus_criados:
                self.menu_bar.entryconfigure(menu, state = 'normal')
            self.tela_login.destroy()

