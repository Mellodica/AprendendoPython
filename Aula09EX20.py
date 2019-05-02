"""
Sorteando nome de uma Lista
"""
import random

n1 = str(input("Primeiro Aluno: "))
n2 = str(input("Segundo Aluno: "))
n3 = str(input("Terceiro Aluno: "))

lista = [n1, n2, n3]

random.shuffle(lista)

print("O escolhidos na ordem é {}".format(lista))