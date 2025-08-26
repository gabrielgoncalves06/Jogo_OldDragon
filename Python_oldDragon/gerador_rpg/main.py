# Importando os componentes
from componentes.dado import Dado
from componentes.gerador_atributos import Gerador
from personagem import Personagem

from racas.anao import Anao
from racas.humano import Humano
from racas.elfo import Elfo

from classes_personagem.guerreiro import Guerreiro
from classes_personagem.mago import Mago
from classes_personagem.ladrao import Ladrao

def selecionar_opcao(opcoes: dict, titulo: str):
    while True:
        print(f"\n --{titulo}")
        for chave, classe in opcoes.items():
            print(f" {chave}: {classe().nome}")

        escolha = input(">> ")
        if escolha in opcoes:
            return opcoes[escolha]()
        print("Opção inválida!")

def main():
    print("Bem-vindo ao Gerador de Personagens estilo Old Dragon!")

    #Dicionário para mapear a escolha do Usuário às classes
    estilos_atributos = {
        "1": "Clássico",
        "2": "Aventureiro",
        "3": "Heróico"
    }

    racas_disponiveis = {'1':Humano,'2':Anao, '3':Elfo}                      # classes
    classes_disponíveis = {'1':Guerreiro,'2': Mago, '3':Ladrao}


    #Instanciando as ferramentas
    dado =Dado()
    gerador = Gerador(dado)
                                                                   # Etapa 1 --------------------------------------------
    while True:
        print("\nEscolha o estilo de distribuição de atributos:")
        for k, v in estilos_atributos.items():
            print(f" {k}: Estilo:{v.capitalize()}")
        print("4 para sair")

        escolha_estilo = input(">>")
        if escolha_estilo == '4':
            print("Até a próxima aventura...")
            break
        if escolha_estilo not in estilos_atributos:
            print("Opção inválida")
            continue

        # --- Seleção de Raça e Classe ---
        raca_escolhida = selecionar_opcao(racas_disponiveis,"Escolha a sua Raça:")         # Etapa 2 --------------------------
        classe_escolhida = selecionar_opcao(classes_disponíveis,"Escolha a sua Classe:")

        #Geração e Montagem---
        nome_personagem = input("\n Dê um nome ao seu novo personagem:  ")

        novo_personagem = Personagem(nome_personagem,raca_escolhida,classe_escolhida)

        #Gera os atributos:

        if escolha_estilo == '1':
            atributos = gerador.gerar_estilo_classico()
        elif escolha_estilo == '2':
            atributos = gerador.gerar_estilo_aventureiro()
        else:
            atributos = gerador.gerar_estilo_heroico()

        # Define os atributos e exibe a ficha final
        novo_personagem.definir_atributos(atributos)
        print("\n" + "=" * 40)
        print("PERSONAGEM CRIADO COM SUCESSO!")
        print("=" * 40)
        print(novo_personagem)
        print("\n")


if __name__ == "__main__":
    main()










