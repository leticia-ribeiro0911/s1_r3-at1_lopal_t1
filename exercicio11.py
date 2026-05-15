# Exercício 11

# Escreva um programa que peça um número de 1 a 10, e mostre a tabuada desse número.

numero = int(input("Digite um número (1 a 10): "))
for i in range(1, 11):
  print(numero, "x", i, "=", numero * i)