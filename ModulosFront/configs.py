from json import dump, load


class Configs:
    def __init__(self, path):
        self.configs_path = path
        self.__inicia_configs()

    def __inicia_configs(self):
        with open(self.configs_path, 'r') as configs_json:
            self.configs: dict = load(configs_json)
            configs_json.close()

    @property
    def __background(self):
        return self.configs['background']

    @property
    def __font(self):
        return self.configs['fonte']

    @property
    def __tamanho_letras(self):
        return self.configs['tamanho_letras']

    @property
    def __fonte_opcoes(self):
        return self.configs['fonte_opcoes']

    @property
    def __bg(self):
        return self.configs['cor_da_borda']

    @property
    def ip_servidor(self):
        return self.configs['ip_servidor']

    @property
    def ultimo_user(self):
        return self.configs['ultimo_user']

    @property
    def nome_da_empresa(self):
        return self.configs['nome_da_empresa']

    @property
    def root_params(self):
        dicio = {
            'background': self.__background,
        }
        return dicio

    @property
    def frames_params(self):
        dicio = {
            'background': self.__bg,
        }
        return dicio

    @property
    def labels_params(self):
        dicio = {
            'background': self.__bg,
            'font': (self.__font, self.__tamanho_letras, self.__fonte_opcoes)
        }
        return dicio

    @property
    def entrys_params(self):
        dicio = {
            'font': (self.__font, self.__tamanho_letras)
        }
        return dicio

    def salvar_config(self, parametros):
        """ Salva no arquivo Json as configurações básicas
        parametros = {
            "nome_da_empresa": str,
            "background": str/hex,
            "fonte": str,
            "tamanho_letras": str,
            "fonte_opcoes": str,
            "bg": str,
            "ip_servidor": str,
            "ultimo_user": str,
        }

        """
        with open(self.configs_path, 'r+') as configs_json:
            for param, value in parametros:
                self.configs[param] = value
                dump(self.configs, configs_json, indent = 2)
            configs_json.close()
