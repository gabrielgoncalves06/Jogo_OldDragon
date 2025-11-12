from .raca_base import Raca
class Halfling(Raca):
    @property
    def nome(self) -> str:
        return "Halfling"

    @property
    def movimento(self) -> int:
        return 6
    @property
    def infravisao(self) -> int:
        return 0

    @property
    def alinhamento_tendencia(self) -> str:
        return "Neutro"

    @property
    def habilidades(self) -> list[str]:
        return [
           "São especialistas em se esconder e em passar despercebidos, conseguindo se esconder com uma chance de 1-2 em 1d6"
           "Os halflings são muito resistentes a efeitos que afetem sua força de vontade",
           "os halflings qualquer ataque à distância com uma arma de arremesso é considerado um ataque fácil."
        ]