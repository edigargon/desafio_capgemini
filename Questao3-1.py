'''
Aproveitei para pegar o exemplo da Questão 3, sobre criptografia,
para mostrar que existe uma biblioteca especifica para esse modo, e irei
utiliza-la aqui, somente para vermos como pode funcionar.
'''

import cryptocode

text = str(input('Informe uma frase: '))
senha = '123456'
text_encry = cryptocode.encrypt(text,senha)
text_decry = cryptocode.decrypt(text_encry,senha)
print(f'O texto cryptografado fica:\n'
      f' {text_encry}\n'
      f'O texto descryptografado volta a ser:\n'
      f'{text_decry}')