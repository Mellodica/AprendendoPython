"""
Crie um programa que leia o nome completo de uma pessoa e mostre:

A) O nome com todas as Letras Maiusculas
B) O Nome do todas as letras minusculas
C) Quantas Letras ao todo sem considerar espaços
D) Quantas Letras tem o Primeiro Nome
"""

#nome = str(input("Digite Seu Nome: "))
nome = 'Helber Aparecido de Oliveira'.strip()
#n1 = nome.strip()
n2 = nome.split()

print("Analisando seu nome...")
print("O Nome em Letras MAIUSCULAS {}".format(nome.upper()))
print("O Nome em Letras MINUSCULAS {}".format(nome.lower()))
print("A Quantidade de Letras no Nome {}".format(len(nome)-nome.count(' ')))
print("A Quantidade de Letras no primeiro Nome {}".format(nome.find(' ')))

print("Seu nome é {} e ele tem {} letras".format(n2[0], len(n2[0])))