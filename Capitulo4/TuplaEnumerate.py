usuarios = {}
resp = "s"
emails = []
while resp == "s":
    emails.append(input("Digite um e-mail: ").lower())
    resp = input("Digite 's' para continuar: ").lower()

tupla = list(enumerate(emails))
for chave in range(0, len(tupla)):
    print("Email: ", tupla[chave][1])
    usuarios[tupla[chave]] = [input("Digite o nome: "), input("Digite o nível: ")]

for chave, dado in usuarios.items():
    print(f'\n~~~~~~~~~ Usuario {chave[0] + 1} ~~~~~~~~~')
    print("Email: ", chave[1])
    print("Nome: ", dado[0])
    print("Nível: ", dado[1])
