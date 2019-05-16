

'''
lista = [1, 2, 3, 5, 10]

for num in lista:
    print(num)
    print(num**2)

 '''
#import random

from random import choice

lista = ['Helber', 'Breno', 'Marcela', 'MAICON DOGRAS']
#escolha = random.choice(lista)

escolha = choice(lista)

print('O Escolhido é {}'.format(escolha))