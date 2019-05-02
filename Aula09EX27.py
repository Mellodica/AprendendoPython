"""
Faca um Programa que leia o completo de uma pessoa e mostre em seguida o primeiro e o ultimo nome separadamente
"""

nome = str(input("Digite seu Nome Completo: ")).strip().upper().split()
#nome = 'Helber Aparecido de Oliveira'
print("Boa Tarde, {}. Tenha uma bom Dia Sr. {}".format(nome[0], nome[len(nome)-1]))
