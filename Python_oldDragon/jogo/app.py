from flask import Flask, render_template, request
from jogo.model.componentes.dado import Dado
from jogo.model.componentes.gerador_atributos import Gerador
from jogo.model.personagem import Personagem

from jogo.model.racas.humano import Humano
from jogo.model.racas.elfo import Elfo
from jogo.model.racas.anao import Anao

from jogo.model.classes_personagem.guerreiro import Guerreiro
from jogo.model.classes_personagem.mago import Mago
from jogo.model.classes_personagem.ladrao import Ladrao

app = Flask(__name__)
gerador = Gerador(Dado())

# 🔹 Listas de opções disponíveis
RACAS = {
    "humano": Humano(),
    "elfo": Elfo(),
    "anao": Anao()
}

CLASSES = {
    "guerreiro": Guerreiro(),
    "mago": Mago(),
    "ladrao": Ladrao()
}


@app.route("/")
def index():
    return render_template("index.html", racas=RACAS, classes=CLASSES)

# 🔹 Criar personagem
@app.route("/criar-personagem", methods=["POST"], endpoint="criar_personagem")
def criar():
    nome = request.form["nome"]
    distribuicao = request.form["distribuicao"]
    raca_escolhida = request.form["raca"]
    classe_escolhida = request.form["classe"]

    # 🔹 Caso o jogador escolha modo aventureiro → redireciona para distribuição manual
    if distribuicao == "aventureiro":
        valores = gerador.gerar_valores_aventureiro()
        return render_template(
            "distribuir.html",
            nome=nome,
            raca_escolhida=raca_escolhida,
            classe_escolhida=classe_escolhida,
            valores=valores,
            atributos=Gerador.ATRIBUTOS_BASE
        )

    # 🔹 Clássico ou Heróico → gera direto
    if distribuicao == "classico":
        atributos = gerador.gerar_estilo_classico()
    elif distribuicao == "heroico":
        atributos = gerador.gerar_estilo_heroico()
    else:
        atributos = {}

    raca = RACAS.get(raca_escolhida)
    classe = CLASSES.get(classe_escolhida)
    personagem = Personagem(nome, raca, classe)
    personagem.definir_atributos(atributos)

    return render_template("resultado.html", personagem=personagem)


# 🔹 Nova rota para finalizar distribuição manual
@app.route("/finalizar-distribuicao", methods=["POST"])
def finalizar_distribuicao():
    nome = request.form["nome"]
    raca_escolhida = request.form["raca"]
    classe_escolhida = request.form["classe"]

    atributos = {}
    for atr in Gerador.ATRIBUTOS_BASE:
        atributos[atr] = int(request.form[atr])

    raca = RACAS.get(raca_escolhida)
    classe = CLASSES.get(classe_escolhida)
    personagem = Personagem(nome, raca, classe)
    personagem.definir_atributos(atributos)

    return render_template("resultado.html", personagem=personagem)


if __name__ == "__main__":
    app.run(debug=True)
