"""
f) faça um programa que pergunte quanto vc ganha por hora e o numero de horas trabalhadas no mês. Calcule e mostre
o total do seu salario no mes.
"""

s = float(input('Qual o seu salario por hora: '))
h = float(input('Quantas horas você trabalha por mês: '))

print('O seu salario é de {:.2f} por mês!'.format(s*h))