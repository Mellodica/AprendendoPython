"""
    Faca um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados

"""

num = (input("Digite um Numero: "))


print("Unidade {}".format(num[3]))
print("Dezena {}".format(num[2]))
print("Centena {}".format(num[1]))
print("Milhar {}".format(num[0]))

print("O Valor da Unidade é {} O Valor da Dezena é {}". format(num[3], num[2]))