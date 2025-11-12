from .raca_base import Raca
class Elfo(Raca):
    @property
    def nome(self) -> str:
        return "Elfo"

    @property
    def movimento(self) -> int:
        return 9
    @property
    def infravisao(self) -> int:
        return 18

    @property
    def alinhamento_tendencia(self) -> str:
        return "Neutro"

    @property
    def habilidades(self) -> list[str]:
        return [
            "Infravisão 18m",
            "Detectar passagens secretas, armadilhas, inclinações e construções de pedra com perícia.",
            "Graciosos: recebem +1 em testes de destreza (JPD).",
            "Arma Racial: bônus de +1 no dano com arcos.",
            "Imunidades: imunes a sono mágico e à paralisia de ghouls."
        ]