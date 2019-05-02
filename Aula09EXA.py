"""
Crie um programa que leia o nome completo de uma pessoa e mostre:

A) O nome com todas as Letras Maiusculas
B) O Nome do todas as letras minusculas
C) Quantas Letras ao todo sem considerar espaços
D) Quantas Letras tem o Primeiro Nome
"""

#nome = str(input("Digite Seu Nome: "))
nome = 'Helber Aparecido de Oliveira'
n1 = nome.strip()
n2 = nome.split()
print("O Nome em Letras MAIUSCULAS {}".format(nome.upper()))
print("O Nome em Letras MINUSCULAS {}".format(nome.lower()))
print("A Quantidade de Letras no Nome {}".format(len(n1)))
print("A Quantidade de Letras no primeiro Nome {}".format(len(n2)))