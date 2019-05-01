"""
Faca um programa que leia um Angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo.

"""

import math

an = float(input("Digite o Valor do Angulo: "))

seno = math.sin(math.radians(an))
cos = math.cos(math.radians(an))
tan = math.tan(math.radians(an))

print("O Ângulo de {} tem o Seno de {:.2f}".format(an, seno))
print("O Ângulo de {} tem o Cosseno de {:.2f}".format(an, cos))
print("O Ângulo de {} tem a Tangente de {:.2f}".format(an, tan))