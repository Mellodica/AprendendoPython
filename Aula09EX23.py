"""
    Faca um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados

"""

num = int(input("Digite um Numero: "))
num1 = str(num)

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

#print("Unidade {}".format(num1[3]))
#print("Dezena {}".format(num1[2]))
#print("Centena {}".format(num1[1]))
#print("Milhar {}".format(num1[0]))

#print("O Valor da Unidade é {} O Valor da Dezena é {}". format(num1[3], num1[2]))

print("Unidade {}".format(u))
print("Dezena {}".format(d))
print("Centena {}".format(c))
print("Milhar {}".format(m))

