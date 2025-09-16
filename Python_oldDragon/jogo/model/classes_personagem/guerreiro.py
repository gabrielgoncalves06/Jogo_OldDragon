from .classe_base import ClassePersonagem

class Guerreiro(ClassePersonagem):
    @property
    def nome(self) -> str:
        return "Guerreiro"

    @property
    def dado_vida(self) -> str:
        return "d8"

    @property
    def atributo_primario(self) -> str:
        return "FOR"

    @property
    def habilidades_de_classe(self) -> list[str]:
        return [
            "Pode usar qualquer arma e armadura.",
            "Recebe +1 em jogadas de ataque e dano a cada 3 níveis."
        ]
    

