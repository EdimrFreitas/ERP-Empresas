from os.path import abspath
from json import dump, load


class Configs:
    configs_path = abspath('./Configs/configs.json')

    def inicia_configs(self):
        with open(self.configs_path, 'r') as configs_json:
            self.configs: dict = load(configs_json)
            configs_json.close()

    def salvar_config(self, param, value):
        with open(self.configs_path, 'r+') as configs_json:
            self.configs[param] = value
            dump(self.configs, configs_json, indent = 2)
            configs_json.close()

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
        return self.configs['bg']

    @property
    def root_params(self):
        dicio = {
            'background': self.__background,
            # 'font': (self.__font, self.__tamanho_letras, self.__fonte_opcoes)
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
