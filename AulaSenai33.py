
"""
h)
Joao Papo de Pescador, homem de bem, comprou um computador para controlar o rendimento diário de seu trabalho.
Toda vez que ele traz um peso de peixe maior que o estabelecido pelo regulamento de pesca do estado de SP
(50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente.
João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso.
GRavar na variavel excessoa quantidade de quilos além do limite e na variavel multa o valor da multa que joão deverá pagar.
imprima os dados do programa com as mensagens adequadas.
"""

p = float(input('Digite o peso do peixe: '))

if p > 50:
    print('O Valor da Multa é {} reais'.format((p-50)*4))

else:
    print('Não há multa para ser paga!')