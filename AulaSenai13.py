"""
Escreva um programa que pergunte a velocidade do carro de um usuário.
Caso a velocidade ultrapasse 80km/h, exiva uma mensagem dizendo que o usuario foi multado.
Nesse caso exiba o valor da Multa cobrado de R$ 5,00 por km acima de 80km/h
"""

km = int(input("Qual a Velocidade do Carro: "))

if km > 80:
    print("Você foi multado em {} reais".format((km-80)*5))

if km <= 80:
    print("Siga Viagem com Tranquilidade!")