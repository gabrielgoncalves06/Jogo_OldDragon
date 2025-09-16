from abc import ABC , abstractmethod

class Raca(ABC):
    @property
    @abstractmethod
    def nome(self) -> str:
        pass

    @property
    @abstractmethod
    def movimento(self) -> str:
        pass

    @property
    @abstractmethod
    def infravisao(self) -> str:
        pass

    @property
    @abstractmethod
    def alinhamento_tendencia(self) -> str:
        pass

    @property
    @abstractmethod
    def habilidades(self) -> list[str]:
        pass