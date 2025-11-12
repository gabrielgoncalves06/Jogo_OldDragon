# models/gerenciador_save.py
import json
import os
from model.classes_personagem.personagem import Personagem 

PASTA_SAVES = "saves"

def salvar_personagem_json(personagem: Personagem):
    """
    Recebe uma instância de Personagem, a converte para um dicionário
    e a salva em um arquivo .json.
    """
    # Cria a pasta 'saves' se ela não existir
    os.makedirs(PASTA_SAVES, exist_ok=True)

   
    personagem_dict = personagem.to_dict()   # Converte o objeto

    # Cria um nome de arquivo seguro (ex: "Aragorn" -> "saves/aragorn.json")
    nome_arquivo = f"{personagem.nome.lower().replace(' ', '_')}.json"
    caminho_arquivo = os.path.join(PASTA_SAVES, nome_arquivo)

    print(f"Salvando personagem em: {caminho_arquivo}")

    # Abre o arquivo e salva o JSON
    with open(caminho_arquivo, 'w', encoding='utf-8') as f:
        json.dump(personagem_dict, f, ensure_ascii=False, indent=4)      # indent=4 deixa o arquivo JSON bonito e legível