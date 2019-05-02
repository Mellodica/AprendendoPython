"""
    Faca um programa que leia o comprimento de um cateto oposto e do cateto adjacente de um triangulo retangulo.
    Calcule e mostre o comprimento da hipotenusa.


"""
from math import pow, sqrt

catOposto = float(input("Digite o Valor do Cateto Oposto: "))
catAdjacente = float(input("Digite o Valor do Cateto Adjacente: "))

rHipotenusa = (pow(catOposto,2) + pow(catAdjacente,2))
hipotenusa = sqrt(rHipotenusa)

print("O Valor da Hipotenusa é {:.2f},". format(hipotenusa))

