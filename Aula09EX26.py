"""
Faca um programa que leia uma Frase pelo teclado e mostre:
A) Quantas vezes aparece a LETRA "A"?
B) Em que posição ela aparece a primeira vez?
C) Em que posição ela aparece pela a ultima vez?
"""

frase = input("Digite uma Frase: ")

print("Existe na Frase {} Letras 'A'".format(frase.count('a')))
print("A Letra 'A' aparece a primeira vez no Indice {}".format(frase.find('a')))
print("A Ultima vez que a Letra 'A' aparece é no indice {}".format(frase.rfind('a')))