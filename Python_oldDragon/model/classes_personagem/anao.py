from .classe_base import ClassePersonagem


class Guerreiro(ClassePersonagem):
    @property
    def nome(self) -> str:
        return "Guerreiro"

    def dado_vida(self) -> str:
        return ("d8")

    def atributo_primario(self) -> str:
        return "FOR"

    def habilidades_de_classe(self) -> list[str]:
        return [
            "Pode usar qualquer arma e armadura.",
            "Recebe +1 em jogadas de ataque e dano a cada 3 níveis."
        ]


