from flask import Flask, render_template, request
from model.componentes.dado import Dado
from model.componentes.gerador_atributos import Gerador
from model.classes_personagem.personagem import Personagem

from model.racas.humano import Humano
from model.racas.elfo import Elfo
from model.racas.anao import Anao

from model.classes_personagem.guerreiro import Guerreiro
from model.classes_personagem.mago import Mago
from model.classes_personagem.ladrao import Ladrao

from gerenciadobd import adicionar_personagem_save
from model.gerenciador_save import salvar_personagem_json


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

   # salvar personagem json
    salvar_personagem_json(personagem)

    adicionar_personagem_save(nome, distribuicao, raca_escolhida, classe_escolhida,atributos)
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

    adicionar_personagem_save(nome,"aventureiro", raca_escolhida, classe_escolhida,atributos)

    # salvar personagem json
    salvar_personagem_json(personagem)

    return render_template("resultado.html", personagem=personagem)


if __name__ == "__main__":
    app.run(debug=True)
