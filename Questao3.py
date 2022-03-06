'''
Um texto precisa ser encriptado usando o seguinte esquema.
Primeiro, os espaços são removidos do texto. Então, os caracteres são
escritos em um grid, no qual as linhas e colunas tem as seguintes regras:

√T<=linha<=coluna<=√T

 * Considere T, como o tamanho do texto.
 * Se certifique de que linhas x colunas >= .
 * Se múltiplos grids satisfazem as condições, escolha aquele com a menor área.

Escreva um algoritmo que ao receber uma string s, mostre a mensagem encriptada
de acordo com as regras descritas.

Exemplo 1:
Entrada: s = tenha um bom dia
Saida: taoa eum nmd hbi

Explicação: Depois de remover os espaços, a string tem 13 caracteres.
√13 está entre 3 e 4, então a string é rescrita na forma de um grid com 4 linhas e 4 colunas:

tenh
aumb
omdi
a

O resultado é obtido ao mostrar os caracteres de cada coluna,
com um espaço entre as colunas de texto. A mensagem encriptada é obtida ao
mostrar os caracteres de cada linha com um espaço entre as colunas.

Exemplo 2:
Entrada: s = ola mundo
Saida: omd luo an

Explicação: Depois de remover os espaços a string tem 8 caracteres.
√8 está entre 2 e 3, então a string é reescrita na forma de um grid com 3 linhas e 3 colunas:

ola
mun
do
'''

# Preparando os dados
import math

matriz = []
i = 0
j = 1

#Recendo o texto
text = input('Nos forneça uma frase: ')

#Remover os espaços do texto
text_sem_espaco = text.replace(" ", "")

#Transformando em um grid
tamanho = len(text_sem_espaco)
#print(tamanho)
raizquadrada = math.sqrt(tamanho)
#print(raizquadrada)
#Verificar se número é float ou int
inteiro = int(raizquadrada)
#Transformando o texto em uma lista
text_lis = list(text_sem_espaco)
#print(text_lis)

if raizquadrada == inteiro:
    for i in range(inteiro):
        matriz.append([0]*inteiro)

    # Criptografando
    if inteiro == 1:
        matriz[0][0] = text_lis[0]
    elif inteiro == 2:
        matriz[0][0] = text_lis[0]
        matriz[0][1] = text_lis[2]
        matriz[1][0] = text_lis[1]
        matriz[1][1] = text_lis[3]
    elif inteiro == 3:
        matriz[0][0] = text_lis[0]
        matriz[0][1] = text_lis[3]
        matriz[0][2] = text_lis[6]
        matriz[1][0] = text_lis[1]
        matriz[1][1] = text_lis[4]
        matriz[1][2] = text_lis[7]
        matriz[2][0] = text_lis[2]
        matriz[2][1] = text_lis[5]
        matriz[2][2] = text_lis[8]
    elif inteiro == 4:
        matriz[0][0] = text_lis[0]
        matriz[0][1] = text_lis[4]
        matriz[0][2] = text_lis[8]
        matriz[0][3] = text_lis[12]
        matriz[1][0] = text_lis[1]
        matriz[1][1] = text_lis[5]
        matriz[1][2] = text_lis[9]
        matriz[1][3] = text_lis[13]
        matriz[2][0] = text_lis[2]
        matriz[2][1] = text_lis[6]
        matriz[2][2] = text_lis[10]
        matriz[2][3] = text_lis[14]
        matriz[3][0] = text_lis[3]
        matriz[3][1] = text_lis[7]
        matriz[3][2] = text_lis[11]
        matriz[3][3] = text_lis[15]
else:
    for i in range(inteiro+1):
        matriz.append([''] * (inteiro+1))

    # Criptografando
    if inteiro+1 == 1:
        matriz[0][0] = text_lis[0]
    elif inteiro+1 == 2:
        matriz[0][0] = text_lis[0]
        matriz[0][1] = text_lis[1]
        matriz[1][0] = text_lis[2]
        matriz[1][1] = text_lis[3]
    elif inteiro+1 == 3:
        matriz[0][0] = text_lis[0]
        matriz[0][1] = text_lis[3]
        matriz[0][2] = text_lis[6]
        matriz[1][0] = text_lis[1]
        matriz[1][1] = text_lis[4]
        matriz[1][2] = text_lis[7]
        matriz[2][0] = text_lis[2]
        matriz[2][1] = text_lis[5]
        #matriz[2][2] = text_lis[8]
    elif inteiro+1 == 4:
        matriz[0][0] = text_lis[0]
        matriz[0][1] = text_lis[4]
        matriz[0][2] = text_lis[8]
        matriz[0][3] = text_lis[12]
        matriz[1][0] = text_lis[1]
        matriz[1][1] = text_lis[5]
        matriz[1][2] = text_lis[9]
        #matriz[1][3] = text_lis[13]
        matriz[2][0] = text_lis[2]
        matriz[2][1] = text_lis[6]
        matriz[2][2] = text_lis[10]
        #matriz[2][3] = text_lis[14]
        matriz[3][0] = text_lis[3]
        matriz[3][1] = text_lis[7]
        #matriz[3][2] = text_lis[11]
        #matriz[3][3] = text_lis[15]

print(matriz)
