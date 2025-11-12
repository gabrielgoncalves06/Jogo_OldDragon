# racas/anao.py
from .raca_base import Raca

class Anao(Raca):
    @property
    def nome(self) -> str:
        return "Anão"

    @property
    def movimento(self) -> int:
        return 6

    @property
    def infravisao(self) -> int:
        return 18

    @property
    def alinhamento_tendencia(self) -> str:
        return "Ordem"

    @property
    def habilidades(self) -> list[str]:
        return [
            "Infravisão 18m",
            "Mineradores: conseguem detectar anomalias em pedras (como armadilhas ou fossos) com facilidade, mesmo sem procurar ativamente.",
            "Vigoroso: recebem +1 em testes de resistência física (JPC).",
            "Armas grandes: anões só podem usar armas pequenas e médias, mas armas grandes forjadas especialmente para eles contam como médias.",
            "Inimigos: ataques contra orcs, ogros e hobgoblins são mais fáceis devido à rivalidade natural."
        ]