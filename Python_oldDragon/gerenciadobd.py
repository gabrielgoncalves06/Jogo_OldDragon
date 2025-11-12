import pymongo
client = pymongo.MongoClient("mongodb://localhost:27017/") #string de acesso ao mondoDB

db = client["PrimeiroBanco"]

collections = db["PrimeiraCollection"]

print("Conexão com o MongoDB estabelecida com sucesso!")

def adicionar_personagem_save(nome, distribuicao, raca_escolhida, classe_escolhida,atributos):
    personagem_save = {
        "nome": nome,
        "distribuicao": distribuicao,
        "raca_escolhida": raca_escolhida,
        "classe_escolhida": classe_escolhida,
        "atributos":atributos
    }
    collections.insert_one(personagem_save)
