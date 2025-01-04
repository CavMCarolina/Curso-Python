from Capitulo4.Funcoes import *

usuarios = {}
acao = perguntar()

while acao != "s":
    if acao == "i":
        inserirUsuario(usuarios)
    elif acao == "p":
        pesquisarUsuario(usuarios)
    elif acao == "e":
        excluirUsuario(usuarios)
    elif acao == "l":
        listarUsuario(usuarios)
    else:
        print("Resposta inválida.")

    acao = perguntar()

print("Saindo....")