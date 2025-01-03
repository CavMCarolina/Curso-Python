inventario = []

# Adicionar itens no inventario
resposta = "sim"
while resposta == "sim":
   equipamento = [input("Equipamento: ").lower(),
                  float(input("Valor: ")),
                  int(input("Número Serial: ")),
                  input("Departamento: ").lower()]
   inventario.append((equipamento))
   resposta = input("Digite 'sim' para continuar: ").lower()

# Exibir dados do inventario
print("\nInventário:")
i = 1
for equipamento in inventario:
    print(f'Equipamento {i}:\n'
          f'Nome: {equipamento[0]}\n'
          f'Valor: {equipamento[1]}\n'
          f'Número Serial: {equipamento[2]}\n'
          f'Departamento: {equipamento[3]}\n')
    i += 1

# Localizar um item no inventario
busca = input("Deseja fazer uma busca? ").lower()
if busca == "sim":
    equipamento_buscado = input("Digite o nome do equipamento que deseja buscar: ").lower()
    print("\nResultado da Busca:")
    for equipamento in inventario:
        if equipamento_buscado == equipamento[0]:
            print(f'\nEquipamento: {equipamento[0]}')
            print("Valor:", equipamento[1])
            print("Número Serial:", equipamento[2])
            print("Departamento:", equipamento[3])

# Depreciar itens no inventario
depreciacao = input("Digite o nome do equipamento que será depreciado: ").lower()
for equipamento in inventario:
    if depreciacao == equipamento[0]:
        print("\nResultado da depreciação:")
        print(f'Equipamento: {equipamento[0]};\nNúmero Serial: {equipamento[2]}')
        print("Valor Antigo:", equipamento[1])
        equipamento[1] = equipamento[1] * 0.9
        print(f'Valor Novo: {equipamento[1]}')

# Excluir um item do inventario
serial_excluido = int(input("Digite a serial do equipamento a ser excluído: "))
i = 0
while i < len(inventario):
    if inventario[i][2] == serial_excluido:
        inventario.remove(inventario[i])
    else:
        i += 1

# Exibir itens do inventario
print("\nInventário:")
i = 1
for equipamento in inventario:
    print(f'Equipamento {i}:\n'
          f'Nome: {equipamento[0]}\n'
          f'Valor: {equipamento[1]}\n'
          f'Número Serial: {equipamento[2]}\n'
          f'Departamento: {equipamento[3]}\n')
    i += 1

# Mostrar o resumo dos valores
valores = []
for equipamento in inventario:
  valores.append(equipamento[1])
if len(valores) > 0:
  print("O equipamento mais caro custa: ", max(valores))
  print("O equipamento mais barato custa: ", min(valores))
  print("O total de equipamentos é de: ", sum(valores))