# Solicite ao usuário que insira o nome de até 7 convidados.
# Armazene os nomes em uma lista.
# Permita ao usuário remover um convidado da lista, caso necessário.
# Exiba a lista final de convidados.

# Digite o nome do convidado 1: João
# Digite o nome do convidado 2: Maria
# ...
# Digite o nome do convidado 7: Pedro
# Deseja remover algum convidado da lista? (sim/não): sim
# Digite o nome do convidado a ser removido: Maria

quant_convidados = 7
nome_convidados = []


for cont in range(quant_convidados):
    nome = input(f"Digite o nome do convidado {cont + 1}: ")
    nome_convidados.append(nome)


remover = input("Deseja remover algum convidado da lista? (sim/não): ").lower()


if remover == 'sim':
    nome_remover = input("Digite o nome do convidado a ser removido: ")
    if nome_remover in nome_convidados:
        nome_convidados.remove(nome_remover)
        print(f"{nome_remover} foi removido da lista.")
    else:
        print(f"{nome_remover} não está na lista de convidados.")


print("Lista final de convidados:", nome_convidados)
