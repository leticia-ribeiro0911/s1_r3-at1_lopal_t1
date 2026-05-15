# Exercício 10

# Utilizando o laço While faça um programa que peça uma senha ao usuário, e que imprima "Acesso liberado" apenas se o usuário digitar a senha corretamente.

# A senha deverá ser a seguinte senha númerica : "676767".

senha = input("Digite a senha: ")
while senha != "676767":
  senha = input("Acesso negado, tente novamente: ")
print("Acesso liberado!")