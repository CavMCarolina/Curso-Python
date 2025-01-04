def preencherInventario(lista):
    resp = "s"
    while resp == "s":
        equipamento = [input("Equipamento: "),
                       float(input("Valor: ")),
                       int(input("Número Serial: ")),
                       input("Departamento: ")]
        resp = input("Digite 's' para continuar: ").lower()
        lista.append(equipamento)

def exibirInventario(lista):
    i = 1
    print("\n~~~~~~~~~~~~~~~~~ Inventário ~~~~~~~~~~~~~~~~~")
    for equipamento in lista:
        print(f'\nEquipamento {i}')
        print("Nome:", equipamento[0])
        print("Valor:", equipamento[1])
        print("Número Serial:", equipamento[2])
        print("Departamento:", equipamento[3])
        i += 1

def localizarItem(lista):
    busca = input("Digite o nome do equipamento que deseja buscar: ").lower()
    print("\n~~~~~~~~~~~~~~~~~ Resultado da Busca ~~~~~~~~~~~~~~~~~")
    for equipamento in lista:
        if busca == equipamento[0]:
            print(f'\nEquipamento: {equipamento[0]}')
            print("Valor:", equipamento[1])
            print("Número Serial:", equipamento[2])
            print("Departamento:", equipamento[3])

def depreciarItem(lista):
    depreciacao = input("Digite o nome do equipamento que será depreciado: ").lower()
    print("\n~~~~~~~~~~~~~~~~~ Resultado da Depreciação ~~~~~~~~~~~~~~~~~")
    for equipamento in lista:
        if depreciacao == equipamento[0]:
            print(f'\nEquipamento: {equipamento[0]};\nNúmero Serial: {equipamento[2]}')
            print("Valor Antigo:", equipamento[1])
            equipamento[1] = equipamento[1] * 0.9
            print(f'Valor Novo: {equipamento[1]}')

def excluirItem(lista):
    serial_excluido = int(input("Digite a serial do equipamento a ser excluído: "))
    for equipamento in lista:
        if equipamento[2] == serial_excluido:
            lista.remove(equipamento)

    return "Itens excluídos"

def resumirValores(lista):
    valores = []
    for valor in lista:
        valores.append(valor[1])
    if len(valores) > 0:
        print("\nO equipamento mais caro custa: ", max(valores))
        print("O equipamento mais barato custa: ", min(valores))
        print("O total de equipamentos é de: ", sum(valores))