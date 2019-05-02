"""
Crie um programa que leia o nome de uma pessoa e diga se ela tem silva no nome
"""

nome = str(input("Digite o Seu Nome: ")).strip()

print("SILVA" in nome.upper())