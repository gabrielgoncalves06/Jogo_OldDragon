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
            #Rola 3 dados de 6 lados
            atributos[atr] = self.dado.Rolar(3,6)
        return atributos

    def gerar_valores_aventureiro(self) -> list[int]:
        valores = []
        for _ in range(6):
          # Rola 4 dados de 6 lados
            valor = self.dado.Rolar(4, 6)
            valores.append(valor)
        return valores

    def gerar_estilo_heroico(self) -> dict:
        # Rola 4 dados de 6 lados, descartando 1 (o menor)
        print("Gerando atributo do estilo heróico (4d6) - 1")
        atributos = {}
        for atr in self.ATRIBUTOS_BASE:
            atributos[atr] = self.dado.Rolar_com_descarte(4,6,1)
        return atributos