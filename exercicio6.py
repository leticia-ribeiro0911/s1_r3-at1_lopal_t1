# Exercício 6

# Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.

# Um número primo é aquele que é divisível somente por ele mesmo e por 1.
# Dica: Utilize o operador aritmético %, que retorna o resto da divisão de dois números.

import time

numero = int(input("Por favor, digite um número inteiro: "))
print("\n")
print("Verificando se o número é primo ou não...")
print("\n")
time.sleep(3)
primo = True
for i in range(2, numero):
  if numero % i == 0:
    primo = False

if primo == True:
  print("O número digitado é primo")
else:
  print("O número digitado não é primo")