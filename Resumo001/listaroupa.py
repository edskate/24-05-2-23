# Criando uma lista de roupas
roupas = ["Camiseta", "Calça", "Vestido", "Jaqueta", "Sapato"]

# Acessando elementos da lista
print(roupas[0])  # Saída: Camiseta
print(roupas[2])  # Saída: Vestido

# Modificando elementos da lista
roupas[1] = "Shorts"
print(roupas)     # Saída: ["Camiseta", "Shorts", "Vestido", "Jaqueta", "Sapato"]

# Adicionando elementos à lista
roupas.append("Blusa")
print(roupas)     # Saída: ["Camiseta", "Shorts", "Vestido", "Jaqueta", "Sapato", "Blusa"]

# Removendo elementos da lista
del roupas[3]
print(roupas)     # Saída: ["Camiseta", "Shorts", "Vestido", "Sapato", "Blusa"]

# Tamanho da lista
print(len(roupas))  # Saída: 5

# Percorrendo a lista com um loop for
for roupa in roupas:
    print(roupa)

# Verificando se uma roupa está na lista
if "Jaqueta" in roupas:
    print("A jaqueta está na lista.")
