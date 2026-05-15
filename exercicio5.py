# Exercício 5

# Faça um programa que leia e valide as seguintes informações:

# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';

nome = input("Por favor, digite o seu nome: ")
while len(nome) <= 3:
  nome = input("Número de caracteres insuficientes, digite novamente:")
idade = int(input("Agora digite a sua idade, por gentileza: "))
while idade < 0 or idade > 150:
  idade = int(input("Idade inválida, digite novamente:"))
salario = float(input("Digite o seu salário: "))
while salario <= 0:
  salario = float(input("Salário inválido, digite novamente:"))
sexo = input("Por favor, digite o seu sexo (f/m): ")
while sexo != "f" and sexo != "m":
  sexo = input("Sexo não identificado, digite novamente: ")
estado = input("Por fim, digite o seu estado civil (s/c/v/d), por favor: ")
while estado != "s" and estado != "c" and estado != "v" and estado != "d":
  estado = input("Estado civil não identificado, digite novamente: ")
print("Dados válidos, agradecemos a sua colaboração!")