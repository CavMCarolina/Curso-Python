equipamento = []
valor = []
serial = []
departamento = []

resposta = "sim"
while resposta == "sim":
    equipamento.append(input("Equipamento: ").lower())
    valor.append(float(input("Valor: ")))
    serial.append(int(input("Número Serial: ")))
    departamento.append(input("Departamento: ").lower())
    resposta = input("Digite 'sim' para continuar: ").lower()

print("\nInventário:")
for i in range(0, len(equipamento)):
    print(f'Equipamento {i + 1}:\n'
          f'Nome: {equipamento[i]}\n'
          f'Valor: {valor[i]}\n'
          f'Número Serial: {serial[i]}\n'
          f'Departamento: {departamento[i]}\n')


busca = input("Deseja fazer uma busca? ").lower()
if busca == "sim":
    equipamento_buscado = input("Digite o nome do equipamento que deseja buscar: ").lower()
    print("\nResultado da Busca:")
    for i in range(0, len(equipamento)):
        if equipamento_buscado == equipamento[i]:
            print(f'\nEquipamento: {equipamento[i]}')
            print("Valor:", valor[i])
            print("Número Serial:", serial[i])
            print("Departamento:", departamento[i])

for i in range(0, len(equipamento)):
    if equipamento[i] == "impressora":
        print("\nResultado da depreciação:")
        print(f'Equipamento: {equipamento[i]};\nNúmero Serial: {serial[i]}')
        print("Valor Antigo:", valor[i])
        valor[i] = valor[i] * 0.9
        print(f'Valor Novo: {valor[i]}\n')

serial_excluido = int(input("Digite a serial do equipamento a ser excluído: "))
i = 0
while i < len(serial):
    if serial[i] == serial_excluido:
        del equipamento[i]
        del departamento[i]
        del valor[i]
        del serial[i]
    else:
        i += 1

print("\nInventário:")
for i in range(0, len(equipamento)):
    print(f'Equipamento {i + 1}:\n'
          f'Nome: {equipamento[i]}\n'
          f'Valor: {valor[i]}\n'
          f'Número Serial: {serial[i]}\n'
          f'Departamento: {departamento[i]}\n')