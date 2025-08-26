from .classe_base import ClassePersonagem


class Mago(ClassePersonagem):
    @property
    def nome(self) -> str:
        return "Mago"

    @property
    def dado_vida(self) -> str:
        return "d4"

    @property
    def atributo_primario(self) -> str:
        return "INT"

    @property
    def habilidades_de_classe(self) -> list[str]:
        return [
            "Pode o Glimório contendo três magias",
            "O Mago pode, uma vez ao dia por nível, decifrar e ler inscrições mágicas, mesmo que não entenda a mensagem."
            "O Mago pode, uma vez ao dia por nível, detectar magia em uma área de 9m + 3m por nível, enquanto se concentra."
        ]



