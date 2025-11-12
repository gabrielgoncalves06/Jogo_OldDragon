import random
class Dado:
    @staticmethod
    def Rolar(quantidade: int,lados: int ) -> int:

        if quantidade <= 0 or lados <= 0:
            return 0
        return sum(random.randint(1,lados) for _ in range(quantidade))

    @staticmethod
    def Rolar_com_descarte(quantidade: int, lados: int, descartar: int) -> int:

        if descartar >= quantidade:
            return 0

        rolagens = [random.randint(1,lados) for _ in range(quantidade)]
        rolagens.sort()


       # Fatiamento da lista para remover os 'descartar' menores
        rolagens_finais = rolagens[descartar:]

        return sum(rolagens_finais)







