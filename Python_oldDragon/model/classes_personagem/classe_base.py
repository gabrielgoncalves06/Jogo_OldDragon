from abc import ABC, abstractmethod


class ClassePersonagem(ABC):
    @property
    @abstractmethod
    def nome(selfself) -> str:
        pass

    @property
    @abstractmethod
    def dado_vida(self) -> str:  # Ex: "d6", "d8"
        pass

    @property
    @abstractmethod
    def atributo_primario(self) -> str: #"FOR" == "FORÇA", "INT" == " INTELIGENCIA"
        pass

    def habilidades_de_classe(self) -> list[str]:
        pass




