
from json import load


class Configs:
    def inicia_configs(self):
        with open('./Configs/configs.json', 'r') as configs_json:
            self.configs = load(configs_json)
            configs_json.close()

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
