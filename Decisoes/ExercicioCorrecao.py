nivel = input("Digite o seu nível: ").lower()

if nivel == "adm" or nivel == "usr":
    genero = input("Insira seu gênero: ").lower()
    if nivel == "adm":
        if genero == "feminino":
            print("Olá, administradora!")
        elif genero == "masculino":
            print("Olá, administrador!")
        else:
            print("Responda o gênero com 'feminino' e 'masculino'")
    else:
        if genero == "feminino":
            print("Olá, usuária!")
        elif genero == "masculino":
            print("Olá, usuário!")
        else:
            print("Responda o gênero com 'feminino' e 'masculino'")
elif nivel == "quest":
    print("Olá, visitante!")
else:
    print("Responda o nível com 'adm', 'usr' ou 'quest'")