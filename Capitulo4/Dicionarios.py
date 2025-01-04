usuarios = {
    "Chaves": ["Chaves Silva","17/06/2017","Recep_01"],
    "Quico": ["Enrico Flores","03/06/2017","Raiox_02"]
    }
# OBS: Se houverem dois objetos com a mesma chave, o último irá sobrescrever o primeiro

# Maneira de adicionar novo objeto
usuarios["Florinda"] = ["Florinda Flores", "26/11/2017", "Recep_01"]

# Exibindo
print(usuarios)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Dados: ", usuarios.get("Chaves"))