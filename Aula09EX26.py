"""
Faca um programa que leia uma Frase pelo teclado e mostre:
A) Quantas vezes aparece a LETRA "A"?
B) Em que posição ela aparece a primeira vez?
C) Em que posição ela aparece pela a ultima vez?
"""

frase = str(input("Digite uma Frase: ")).strip().upper()

print("Existe na Frase {} Letras 'A'".format(frase.count('A')))
print("A Letra 'A' aparece a primeira vez no Indice {}".format(frase.find('A')+1))
print("A Ultima vez que a Letra 'A' aparece é no indice {}".format(frase.rfind('A')+1))