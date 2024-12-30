tabuada = int(input("Digite um número para exibir a tabuada: "))
print("Tabuada do número:", tabuada)
for valor in range(0, 11):
    print(f'{tabuada} x {valor} = {tabuada * valor}')