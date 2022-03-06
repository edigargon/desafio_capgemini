'''
Dado um vetor de inteiros n e um inteiro qualquer x.
Construa um algoritmo que determine o número de elementos pares
do vetor que tem uma diferença igual ao valor de x.

Exemplos:
Entrada: n = [1,5,3,4,2]
Saida: 3

Explicação:
Existem 3 pares de inteiros no vetor com uma diferença de 2: [5, 3], [4, 2] e [3, 1].
'''

#Separando os dados

list = []
n = []
x = 0
cont = 1

# Recebendo os valores

quant = int(input('Determine o número de elementos do vetor: '))

for i in range(quant):
    z = int(input(f'Informe o {i+1}º número do vetor: '))
    n.append(z)
    i = i + 1

x = int(input('Determine o número que será a diferença: '))

# Percorrendo o Vetor

for i in range(len(n)):
    print(n[i])
    list.append([n[i])
    cont = cont + 1




print(list)