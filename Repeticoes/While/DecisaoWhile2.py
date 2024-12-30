resposta = 'sim'

while resposta == 'sim':
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    doenca_infectocontagiosa = input("Suspeita de doença infectocontagiosa? ").lower()

    # primeiro problema a ser resolvido
    while doenca_infectocontagiosa != "sim" and doenca_infectocontagiosa != "nao":
        print("Responda com 'sim' ou 'nao'")
        doenca_infectocontagiosa = input("Suspeita de doença infectocontagiosa? ").lower()

    if doenca_infectocontagiosa == "sim":
        print("Encaminhe o paciente para sala AMARELA")
    else:
        print("Encaminhe o paciente para sala BRANCA")

    # segundo problema a ser resolvido
    if idade >= 65:
        print("Paciente COM prioridade")
    else:
        genero = input("Digite o gênero do paciente: ").lower()
        if genero == "FEMININO" and idade > 10:
            gravidez = input("A paciente está grávida? ").lower()
            if gravidez == "sim":
                print("Paciente COM prioridade")
            else:
                print("Paciente SEM prioridade")
        else:
            print("Paciente SEM prioridade")

    resposta = input("Digite 'sim' para continuar.")