ips = {}
resp = "s"
while resp == "s":
    ips[(input("Digite os dois primeiros octetos: "),
         input("Digite os dois últimos octetos: "))] = input("Nome da máquina: ")
    resp = input("Digite 's' para continuar: ").lower()

print("Exibindo ip´s: ")
for ip in ips.keys():
    print(ip[0] + "." + ip[1])

print("Exibindo máquinas com o mesmo endereço (redes diferentes): ")
pesquisa = input("Digite os dois últimos octetos: ")
for ip, nome in ips.items():
    if (ip[1] == pesquisa):
        print(nome)

print("Exibindo as máquinas que compõem uma mesma rede: ")
rede = input("Digite os dois primeiros octetos: ")
for ip, nome in ips.items():
    if (ip[0] == rede):
        print(nome)
