from requests import Session
from json import loads


class USUARIO:
    def __init__(self, infos):
        self.id_usuario = infos['id_usuario']
        self.status = infos['status']
        self.nome = infos['nome']
        self.usuario = infos['usuario']
        self.senha = infos['senha']
        self.id_perfil = infos['id_perfil']
        self.email = infos['email']

    def __repr__(self):
        return f'Name <{self.nome}>'


class PERFIL:
    def __init__(self, infos):
        self.id_perfil = infos['id_perfil']
        self.perfil = infos['perfil']

    def __repr__(self):
        return f'Perfil <self.perfil>'


class PERMISSOES:
    def __init__(self, infos):
        self.__infos = infos
        self.id_perfil = infos['id_perfil']
        self.cadastro_de_clientes = infos['cadastro_de_clientes']
        self.cadastro_de_produtos = infos['cadastro_de_produtos']
        self.cadastro_de_servicos = infos['cadastro_de_servicos']
        self.cadastro_de_usuarios = infos['cadastro_de_usuarios']
        self.cadastro_de_estoque = infos['cadastro_de_estoque']
        self.vendas = infos['vendas']
        self.clientes_por_regiao = infos['clientes_por_regiao']
        self.compras_por_periodo = infos['compras_por_periodo']
        self.ranking_de_clientes = infos['ranking_de_clientes']
        self.paretto = infos['paretto']

    def __repr__(self):
        return f'ID Perfil <{self.id_perfil}>'

    def __iter__(self):
        modulos = (
            self.cadastro_de_clientes, self.cadastro_de_produtos, self.cadastro_de_servicos,
            self.cadastro_de_usuarios, self.cadastro_de_estoque, self.vendas, self.clientes_por_regiao,
            self.compras_por_periodo, self.ranking_de_clientes, self.paretto
        )
        return iter(modulos)

    @property
    def dicio_permissoes(self):
        return {
            'Cadastro de clientes': self.cadastro_de_clientes,
            'Cadastro de produtos': self.cadastro_de_produtos,
            'Cadastro de serviços': self.cadastro_de_servicos,
            'Cadastro de usuários': self.cadastro_de_usuarios,
            'Controle de estoque': self.cadastro_de_estoque,
            'Vendas': self.vendas,
            'Clientes por região': self.clientes_por_regiao,
            'Compras por periodo': self.compras_por_periodo,
            'Ranking de clientes': self.ranking_de_clientes,
            'Paretto': self.paretto
        }

    def __len__(self):
        return len(self.__infos)


class ConectorBD:
    def __init__(self, ip='127.0.0.1', usuario=None, senha=None):
        self.__session_obj = Session()
        self.__ip = ip
        self.__logar(usuario, senha)

    @property
    def __servidor(self):
        return 'http://' + self.__ip + ':5000'

    @__servidor.getter
    def __get_servidor(self):
        return self.__servidor

    def __logar(self, usuario, senha):
        url = self.__get_servidor + '/auth'
        payload = dict(usuario = usuario, senha = senha)
        sessao = self.__session_obj.post(url = url, params = payload)

        dicio = loads(sessao.content)

        self.usuario = USUARIO(dicio['user_infos'])
        self.perfil = PERFIL(dicio['perfil_infos'])
        self.permissoes = PERMISSOES(dicio['permissoes_infos'])
        # print(dicio)

    # def consulta(self, tipo: str, filtros: list):
    #     url = self.__get_servidor + '/consulta'
    #
    #     payload = dict(tipo=tipo, filtros=filtros)
    #
    #     return self.__session_obj.get(url=url, json=payload).content
    #
    # def logout(self):
    #     url = self.__get_servidor + '/logout'
    #
    #     return self.__session_obj.get(url=url).text


if __name__ == '__main__':
    usuario = 'Edimar'
    senha = '12345'
    login = ConectorBD(ip = '127.0.0.1', usuario = usuario, senha = senha)

    # info = login.consulta(tipo='usuarios', filtros=['infos1', 'infos2'])
    # print(info)

    # logoff = login.logout()
    # print(logoff)
