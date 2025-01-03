inventario=[]
resposta="sim"
while resposta=="sim":
  inventario.append(input("Equipamento: "))
  inventario.append(float(input("Valor: ")))
  inventario.append(int(input("Número Serial: ")))
  inventario.append(input("Departamento: "))
  resposta=input("Digite 'sim' para continuar: ").lower()

for elemento in inventario:
  print(elemento)