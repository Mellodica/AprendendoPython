"""
g) Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando
as seguintes formulas:
Para Homens (72.7*h)-58
Para Muleheres (62.1*h)44.7
"""

h = float(input('Digite qual sua altura: '))
s = str(input('Digite [M] para mulher [H] para Homem: ')).upper()
if s == 'M':
    print('O peso ideial é {}'.format((62.1*h)-44.7))

if s == 'H':
    print('O peso ideal é {}'.format((72.7*h)-58))