def perguntar():
    resposta = input("\nO que voce deseja fazer?\n"
                 "<i> Para inserir um usuário\n"
                 "<p> Para pesquisar um usuário\n"
                 "<e> Para excluir um usuário\n"
                 "<l> Para listar um usuário\n"
                 "<s> Para sair\n").lower()
    return resposta

def inserirUsuario(dicionario):
    chave = input("Digite o login: ").lower()
    dicionario[chave] = [input("Digite o nome: ").lower(),
                         input("Digite a última data de acesso: ").lower(),
                         input("Digite a última estação acessada: ").lower()]

    print("\nUsuário inserido com sucesso!")

def pesquisarUsuario(dicionario):
    pesquisa = input("Digite o login de quem quer pesquisar: ").lower()
    resultado = dicionario.get(pesquisa)

    if resultado != None:
        print("~~~~~~~~~~~ Usuário Encontrado! ~~~~~~~~~~~")
        print(f'Nome: {resultado[0]}\n'
              f'Último Acesso: {resultado[1]}\n'
              f'Última Estação: {resultado[2]}')
    else:
        print("\nUsuário não encontrado.")

def excluirUsuario(dicionario):
    excluir = input("Digite o login de quem deseja excluir: ").lower()

    if dicionario.get(excluir) != None:
        del dicionario[excluir]
        print(f'\nUsuário Excluído: {excluir}')
    else:
        print("\nUsuário não encontrado.")

def listarUsuario(dicionario):
    i = 1
    print("~~~~~~~~~~~~~ Dicionário ~~~~~~~~~~~~~")
    for chave, dados in dicionario.items():
        print(f'\nObjeto {i}:')
        print(f'Login: {chave}')
        print(f'Dados: {dados}')
        i += 1

