# Exercício 2

# Escreva um script que leia três números e mostre o maior e o menor deles.

maiormenor = input("Digite três números: ")
numero = maiormenor.split(',')
num1 = int(numero[0])
num2 = int(numero[1])
num3 = int(numero[2])
if num1 > num2 and num3:
 maior = num1
if num2 > num1 and num3:
 maior = num2
if num3 > num1 and num2:
 maior = num3

if num1 < num2 and num3:
 menor = num1
if num2 < num1 and num3:
 menor = num2
if num3 < num1 and num2:
 menor = num3
print(f"o maior numero dos tres que voce digitou é {maior}, e o menor é {menor}")