# String
nome = input("Digite um funcionário: ")
empresa = input("Digite a instituição: ")

# int
qtde_funcionarios = int(input("Digite a qtde de funcionários: "))

# float
mediaMensalidade = float(input("Digite a média da mensalidade: "))

print(nome + " trabalha na empresa " + empresa)
# print sem precisar transformar em string:
print("Possui:", qtde_funcionarios," funcionarios.") # Com , ... , nao precisa de espacos no print
# ao usar o '+' precisa transformar em string
print("A média da mensalidade é de: " + str(mediaMensalidade))

print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\nVerifique os tipos de dados abaixo:\n")
print("O tipo de dado da variavel 'nome' é: ",type(nome))
print("O tipo de dado da variavel 'empresa' é: ",type(empresa))
print("O tipo de dado da variavel 'qtde_funcionarios' é: ",type(qtde_funcionarios))
print("O tipo de dado da variavel 'mediaMensalidade' é: ",type(mediaMensalidade))