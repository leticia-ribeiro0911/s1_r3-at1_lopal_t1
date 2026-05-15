# Exercício 4

# A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... (o próximo termo, a partir do terceiro (número 2), é sempre gerado a partir do somatório dos últimos dois). Faça um programa capaz de gerar a série até o n−ésimo termo (onde o valor n deve ser inserido pelo usuário).

num = int(input("Digite a quantidade de termos: "))
termo1 = 1
termo2 = 1
print(termo1)
print(termo2)
for i in range(num - 2):
  termo3 = termo1 + termo2
  print(termo3)
  termo1 = termo2
  termo2 = termo3