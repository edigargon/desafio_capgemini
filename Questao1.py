'''
A mediana de uma lista de números é basicamente o elemento que se encontra no meio da lista
após a ordenação. Dada uma lista de números com um número ímpar de elementos, desenvolva um
algoritmo que encontre a mediana.

Exemplo:
Entrada : arr = [9,2,1,4,6]
Saida: 4
'''

# Pedindo ao usuário a quantidade de elementos para a lista

quant = 0
cont = 0
list = []

while quant % 2 == 0:
    z = int(input('Informe a quantidade de digitos que quer na lista: '))
    print('Somente Números Impares')
    quant = z


# Informando os elementos para a lista
while cont != quant:
    x = input(f'Informa o {cont+1}º número: ')
    list.append(x)
    cont = cont + 1

#Ordenando a lista
list.sort()

#Encontrando a Mediana

#Pegamos o tamanho da lista
tamanho = len(list)

#Dividimos somente inteiros, para pegarmos a metade do tamanho.
#OBS: Como a lista começa do 0, temos o número da meio, se dividirmos por 2.
y = tamanho//2

#Imprime o meio da lista
print(list[y])

