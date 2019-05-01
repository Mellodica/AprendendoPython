'''
Crie um programa que leia um numero Real qualquer pelo teclado e mostre na tela a sua porcao inteira.
EX: Digite 6.127. O Número 6.127 tem a parte inteira 6.
'''


#importando a Biblicoteca especifica TRUNC da Funcão math MATEMATICA
from math import trunc

num = float(input("Digite um Valor Acima de Hum Mil com ponto: "))

                                                #importação TRUNC, nao precisa usar MATH antes
print("O Valor inteiro Digitado é, {} o seu Inteiro é {}".format(num, trunc(num)))