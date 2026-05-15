# Exercício 7

# Faça um algoritmo utilizando o laço FOR que descreva o Fatorial de um número digitado pelo usuário.

import math

numero = int(input("Digite um número: "))
fatorial = 1
for i in range(1, numero + 1):
  fatorial = fatorial * i
print(f"O fatorial do número que você digitou é: {fatorial}")