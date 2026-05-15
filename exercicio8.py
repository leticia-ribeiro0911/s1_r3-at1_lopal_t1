# Exercício 8

# Dada a lista

# L = [5, 7, 2, 9, 4, 1, 3]

# Escreva um programa que imprima as seguintes informações:

# a) tamanho da lista.

# b) maior valor da lista.

# c) menor valor da lista.

# d) soma de todos os elementos da lista.

# e) lista em ordem crescente.

# f) lista em ordem decrescente.

L = [5, 7, 2, 9, 4, 1, 3]
print(f"O tamanho da lista é:", len(L))
print(f"O maior valor da lista é:", max(L))
print(f"O menor valor da lista é:", min(L))
print(f"A soma dos elementos da lista é:", sum(L))
L.sort()
print("A ordem crescente é:", L)
L.sort(reverse=True)
print("A ordem decrescente é:", L)