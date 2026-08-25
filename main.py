import os
import json

if os.path.exists("bd.json"):
    with open("bd.json", "r") as arquivo:
        k = json.load(arquivo)
else:
    k = {
        "afazer": [],
        "analise": [],
        "desenvolvimento": [],
        "teste": [],
        "finalizado": []
    }

print(f"KANBAN")
print(f"1 - VISUALIZAR")
print(f"2 - ADICIONAR")
print(f"3 - MOVER")
print(f"4 - EXCLUIR")
print(f"5 - RESETAR")

opc = int(input(f"Oque deseja fazer?: "))
if opc ==1:
    print(k)
elif opc ==2:
    texto = input("Oque voce quer adicionar em A Fazer?: ")
    k["afazer"].append(texto)
elif opc ==3:
    print("Voce escolheu mover!!")
    for i,col in enumerate(k):
        print(f"{i+1} = {col}")
    coluna = int(input("Qual coluna voce deseja mover?"))
    coluna_mover = list(k.keys())[coluna-1]
    print(f"Voce escolheu mover os itens da coluna: {coluna_mover}")

    for i,item in enumerate(k[coluna_mover]):
        print(f"{i+1} = {item}")
    escolha_item = int(input("Qual item deseja mover?: "))-1

    for i,col in enumerate(k):
        print(f"{i+1} = {col}")
    coluna2 = int(input(f"Em qual coluna voce deseja mover o '{k[coluna_mover][escolha_item]}'?: "))
    coluna_receber = list(k.keys())[coluna2-1]
    print(f"Voce escolheu mover {k[coluna_mover][escolha_item]} para coluna: {coluna_receber}")

    item = k[coluna_mover].pop(escolha_item)
    k[coluna_receber].append(item)

elif opc == 4:
    print("Você escolheu excluir!")

    for i, col in enumerate(k):
        print(f"{i+1} = {col}")

    coluna = int(input("De qual coluna deseja excluir? "))
    coluna_excluir = list(k.keys())[coluna - 1]

    print(f"\nItens da coluna {coluna_excluir}:")

    for i, item in enumerate(k[coluna_excluir]):
        print(f"{i+1} = {item}")

    escolha_item = int(input("Qual item deseja excluir? ")) - 1
    item = k[coluna_excluir].pop(escolha_item)

    print(f"Item '{item}' excluído com sucesso!")


elif opc == 5:
    print("Você escolheu RESETAR o Kanban!")

    confirmar = input("Tem certeza? (s/n): ").lower()

    if confirmar == "s":
        for coluna in k:
            k[coluna] = []

        print("Kanban resetado com sucesso!")
    else:
        print("Reset cancelado.")
        

    
with open("bd.json", "w") as arquivo:
    json.dump(k, arquivo, indent=4)