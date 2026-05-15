# Exercício 3

# Faça um algoritmo que imprima o nome digitado pelo usuário na vertical em escada.

# Exemplo:

# F

# FU

# FUL

# FULA

# FULAN

# FULANO

nome = input("Digite um nome: ")
nome = nome.upper()
for i in range(len(nome) + 1):
  print(nome[:i])