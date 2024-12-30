nivel = input("Digite o seu nível: ").lower()

if nivel == "adm" or nivel == "usr":
    genero = input("Insira seu gênero: ").lower()
    if genero == "feminino":
        if nivel == "adm":
            print("Olá, administradora!")
        else:
            print("Olá, usuária!")
    elif genero == "masculino":
        if nivel == "adm":
            print("Olá, administrador!")
        else:
            print("Olá, usuário!")
    else:
        print("Responda o gênero com 'feminino' e 'masculino'")
elif nivel == "quest":
    print("Olá, visitante")
else:
    print("Responda o nível com 'adm', 'usr' ou 'quest' ")