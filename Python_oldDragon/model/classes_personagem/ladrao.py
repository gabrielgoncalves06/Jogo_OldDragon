from .classe_base import ClassePersonagem


class Ladrao(ClassePersonagem):
    @property
    def nome(self) -> str:
        return "Ladrao"

    @property
    def dado_vida(self) -> str:
        return "d6"

    @property
    def atributo_primario(self) -> str:
        return "DES"

    @property
    def habilidades_de_classe(self) -> list[str]:
        return [
            "O Ladrão que ataca um inimigo furtivamente pode realizar um ataque muito fácil",
            "O Ladrão tem uma chance aprimorada de ouvir ruídos, como conversas atrás de portas ou a aproximação de monstros"

        ]


