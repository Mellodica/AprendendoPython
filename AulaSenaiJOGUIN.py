import random
import numpy


print("O Jogo esta pronto para começar!\n")
print(("VALENNNNDOOOOO!!!!\n\n"))

lista = random.randrange(0, 20)
print("Qual número estou pensando!?")

n1 = int(input("Digite um número entre 0 e 20!!\n\n\t\t"))

while n1 != lista:
    if lista > n1:
        n1 = int(input("Errouuuu!! Tente um número maior que este!!!! \n\n\n"))
    elif lista < n1:
        n1 = int(input("Errrrooouuuu!!! Tente um número menor que ESTE!!\n\n\n"))

if lista == n1:
    print("Para-BENS! Você acertou o número que eu estava pensando!")






