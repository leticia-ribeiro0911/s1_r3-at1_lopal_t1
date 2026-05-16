# Descrição dos exercícios

### Exercício 1 
 Faça um algoritmo usando o for para mostrar os números pares e impares de 0 a 100.
<img width="797" height="167" alt="image" src="https://github.com/user-attachments/assets/12146398-50ce-4963-8181-0d3b1e7fbd0e" />
 - #### Descrição:
   Nesse código foi usado o "for" junto com o "range(101)", que é para o código contar do 0 até o 100, por isso o "(101)". Depois, foi utilizado o "if" com o "% 2 == 0", que é para ver se o resto da divisão dos números por 2 é igual a zero. Se o resto da divisão for igual a zero, o número é par, e se não for igual (else) a zero, ele é ímpar.

### Exercício 2
 Escreva um script que leia três números e mostre o maior e o menor deles.
<img width="803" height="376" alt="image" src="https://github.com/user-attachments/assets/31bed582-b09b-44e2-87b8-60fa27d2e32d" />
- #### Descrição:
  O código acima foi utilizado o "if", que é como um "SE tal coisa for maior que o assim assado, então tal coisa é igual ao assado assim" (como se fosse), nesse código ele foi usado para que fosse possível identificar o maior e o menor número, de três números que fosse digitado, o que lembra a estrutura do código que fizemos em outro exercício, onde tinhamos que deixar os números em ordem crescente, se eu não me engano.

### Exercício 3
 Faça um algoritmo que imprima o nome digitado pelo usuário na vertical em escada.

Exemplo:

F

FU

FUL

FULA

FULAN

FULANO

<img width="400" height="91" alt="image" src="https://github.com/user-attachments/assets/50033561-9ae1-4bd9-b24d-cc2b5eadef7e" />

- #### Descrição:
  Nesse algoritmo, foi usado o "for" e o "range" novamente, porém com o "(len(nomedavariavel) + 1) na frente do range, que serve para criar um loop que vai de 0 até o tamanho do nome escrito, e o "+1" é para colocar o nome inteiro na última impressão, fazendo com que fosse possível mostrar o nome crescendo letra por letra, assim como pede o exercício.

### Exercício 4
 A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... (o próximo termo, a partir do terceiro (número 2), é sempre gerado a partir do somatório dos últimos dois). Faça um programa capaz de gerar a série até o n−ésimo termo (onde o valor n deve ser inserido pelo usuário).

 <img width="521" height="204" alt="image" src="https://github.com/user-attachments/assets/ab18d235-c191-4ff1-ab12-efb05a84c35f" />

- #### Descrição:
  Este código da série de Fibonacci, começa com o "termo1" e o "termo2" que são os dois primeiros valores, depois é utilizado o "for" com o "range(num - 2)" para a repetição  dos próximos números, mas sem repetir os últimos dois, pois já foram mostrados antes. Ai em cada repetição o algoritmo soma os dois últimos primeiros termos, para formar o próximo termo (termo3).

### Exercício 5
   Faça um programa que leia e valide as seguintes informações:
  
- Nome: maior que 3 caracteres;
- Idade: entre 0 e 150;
- Salário: maior que zero;
- Sexo: 'f' ou 'm';
- Estado Civil: 's', 'c', 'v', 'd';

<img width="525" height="318" alt="image" src="https://github.com/user-attachments/assets/eb9f636b-ef4e-4a17-b38a-c79bd55d9cec" />

- #### Descrição:
  Esse código serve para validar os dados que foram digitados, para ver se estão certos ou errados, usando o "input" para pegar esses dados e o "int" e o "float" para transformar as respostas em números. Já o "while" tem como funcionalidade o looping, ou seja, vai fazer o algoritmo ficar repetindo as perguntas caso as respostas forem inseridas incorretamente. E para testar os erros, no algoritmo é utilizado o "or", o "and" e o "!=" (!= significa diferente).

### Exercício 6
 Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.

- Um número primo é aquele que é divisível somente por ele mesmo e por 1.

Dica: Utilize o operador aritmético %, que retorna o resto da divisão de dois números.

<img width="525" height="321" alt="image" src="https://github.com/user-attachments/assets/40b56d80-f01f-4fd8-9cc3-f08e6483cf56" />
  
- #### Descrição:
  Nesse código eu importei o "time" e usei o "time.sleep(3)" para parecer que o código está pensando antes de dar a resposta e fazer uma graça. Em seguida foi criado a variável "primo = True", porque o "range(2, numero):" serve para testar as divisões do número por todos os outros números a partir do 2, ai se a divisão não der zero, "primo" será verdade, mas se der zero o "primo" será falso (no caso, não é um número primo).

### Exercício 7
 Faça um algoritmo utilizando o laço FOR que descreva o Fatorial de um número digitado pelo usuário.

 <img width="527" height="150" alt="image" src="https://github.com/user-attachments/assets/c82cdc29-7df2-4315-94d1-a9326444c15f" />

- #### Descrição:
  Dentro desse código é utilizado o "for" (loop), com o "range(1, numero + 1):" que é para passar por todos os números de 1 até o número que foi digitado, e ai dentro do loop ele vai multiplicando o valor atual de fatorial pelo número "i" da vez.

### Exercício 8
 Dada a lista

L = [5, 7, 2, 9, 4, 1, 3]

Escreva um programa que imprima as seguintes informações:

a) tamanho da lista.

b) maior valor da lista.

c) menor valor da lista.

d) soma de todos os elementos da lista.

e) lista em ordem crescente.

f) lista em ordem decrescente.

<img width="511" height="183" alt="image" src="https://github.com/user-attachments/assets/b2a7c4c5-dcf3-4fca-aa95-d63f94a2aaa5" />

- #### Descrição:
  Esse código organiza uma lista, chamada "L", usando funções prontas, começando pelo "len" que serve para contar quantos números da lista tem, já o "max" e o "min" são para achar o maior (max), e o menor (min) valor dentro da lista, também foi usado o "sum", usado para somar todos os elementos da lista, e por fim o "L.sort", e o "L.sort(reverse=True", que serviram para ordenar os números da lista em ordem crescente e decrescente.

### Exercício 9
 Dada a tabela em anexo , crie um dicionário que a represente.

 <img width="519" height="163" alt="image" src="https://github.com/user-attachments/assets/e8a5a6c5-6bf0-4180-84f7-b6a5ca82403f" />

- #### Descrição:
  Neste código foi criado uma estrutura de dados chamada de "dicionário" para representar o cardápio de uma lanchonete, ele usa as chaves {} para abrir e fechar o dicionário e também serve para organizar as informações no esquema de chave e valor, onde o produto (chave) fica do lado esquerdo, e o preço (valor) fica do lado direito.

### Exercício 10
 Utilizando o laço While faça um programa que peça uma senha ao usuário, e que imprima "Acesso liberado" apenas se o usuário digitar a senha corretamente.

A senha deverá ser a seguinte senha númerica : "676767".

<img width="518" height="93" alt="image" src="https://github.com/user-attachments/assets/657ba372-60f9-44cd-8bd7-3ca06e98850d" />

- #### Descrição:
  Nesse algoritmo foi usado o while para criar um looping que verifica se a senha digitada é diferente (!=) de "676767", porque se for ele irá falar "Acesso Negado" (senha incorreta) e perguntar qual é a senha, novamente.

### Exercício 11
 Escreva um programa que peça um número de 1 a 10, e mostre a tabuada desse número.

 <img width="508" height="72" alt="image" src="https://github.com/user-attachments/assets/42c30394-6b80-4c83-9c30-413ab2820353" />

- #### Descrição:
  E por fim, esse código utiliza o comando "for i in range(1, 11)" que cria um laço de repetição que passa por todos os números de 1 até o 10, ai dentro desse laço, o "print" vai imprimir as linhas, uma por uma, com o numero fixo (x), o valor atual (i) e o resultado da multiplicação entre o número e o "i".
