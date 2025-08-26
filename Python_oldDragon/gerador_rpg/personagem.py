from racas.raca_base import Raca
from classes_personagem.classe_base import ClassePersonagem

class Personagem:

    """ Representa o personagem final, compondo seus atributos,
        raça e classe.
    """
    #CONSTRUTOR
    def __init__(self,nome: str, raca: Raca, classe: ClassePersonagem):
        self.nome = nome
        self.raca = raca
        self.classe = classe
        self.atributos = {
            "FOR": 0,"DES": 0, "CON": 0,
            "INT": 0,"SAB": 0, "CAR": 0
        }



    def definir_atributos(self, atributos: dict):
        self.atributos.update(atributos)

    def __str__(self) -> str:
        texto = f"----Ficha do Personagem ----------\n"
        texto+= f"Nome: {self.nome}\n"
        texto+= f"raca: {self.raca.nome}\n"
        texto+= f"Classe: {self.classe.nome}\n"
        texto+= f" -------Atributos------------\n"
        for atributo, valor in self.atributos.items():
            texto+= f" {atributo}: {valor:<3} "
        texto+= f"\n---Características Raciais--------\n"
        texto+= f"Movimento: {self.raca.movimento}\n"
        texto+= f"Alinhamento: {self.raca.alinhamento_tendencia}\n"
        texto+= f"\n------Habilidade:-----------------\n"
        for hab in self.raca.habilidades:
            texto+= f" - {hab}\n"

        texto +="\n ---Características da Classe ------\n"
        texto += f" | Dado de vida: {self.classe.dado_vida}\n"
        texto += f" | Atributo Primário: {self.classe.atributo_primario}\n"
        texto += f" | Habilidades: \n"
        for hab in self.classe.habilidades_de_classe:
            texto +=  f"  -- {hab}\n"

        texto += f" ------------------------------------------"
        return texto














