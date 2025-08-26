from .dado import Dado


class Gerador:

    ATRIBUTOS_BASE = ["FOR", "DES", "CON", "INT", "SAB", "CAR"]

    def __init__(self, dado : Dado):
        self.dado = dado

    """
       Regra: Role 3d6 para cada atributo.
    """
    def gerar_estilo_classico(self) -> dict:
        print("Gerando atribusto do estilo clásssico! (3d6) ")
        atributos = {}
        for atr in self.ATRIBUTOS_BASE:
            atributos[atr] = self.dado.Rolar(3,6)
        return atributos

    def gerar_estilo_aventureiro(self) -> dict:
        print("Gerando atributo do estilo Aventureiro! (4d6) ")
        atributos = {}
        for atr in self.ATRIBUTOS_BASE:
            atributos[atr] = self.dado.Rolar_com_descarte(4,6,1)
        return atributos

    def gerar_estilo_heroico(self) -> dict:
        print("Gerando atributo do estilo heróico (2d6 + 6) ")
        atributos = {}
        for atr in self.ATRIBUTOS_BASE:
            atributos[atr] = self.dado.Rolar(2,6) + 6
        return atributos








