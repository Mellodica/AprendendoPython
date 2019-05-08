"""
    Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
    Faca um programa que ajuda ele, lendo o Nome deles e escrevendo o nome escolhido.
"""

#import random
from random import choice

n1 = str(input("Primeiro Aluno: "))
n2 = str(input("Segundo Aluno: "))
n3 = str(input("Terceiro Aluno: "))

lista = [n1, n2, n3]

#importar biblioteca toda o código muda para: escolhido = random.choise(lista)
escolhido = choice(lista)

print("O Aluno escolhido foi {}".format(escolhido))
