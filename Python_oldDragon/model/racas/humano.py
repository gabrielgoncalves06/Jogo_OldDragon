from .raca_base import Raca
class Humano(Raca):
    @property
    def nome(self) -> str:
        return "Humano"

    @property
    def movimento(self) -> int:
        return 9
    @property
    def infravisao(self) -> int:
        return 0

    @property
    def alinhamento_tendencia(self) -> str:
        return "Leal ou Neutro"

    @property
    def habilidades(self) -> list[str]:
        return [
            "Aprendizado: recebem +10% de experiência (XP) em todas as situações",
            "Adaptabilidade: ganham +1 em uma Jogada de Proteção (JP) à sua escolha."
        ]