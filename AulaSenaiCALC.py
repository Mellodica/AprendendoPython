

n1 = int(input("Digite o Primeiro Número!\n\t\t\t"))
n2 = int(input("Digite o Segundo Número!\n\t\t\t"))

print("\n Escolha o CALCULO: [SOM], [DIV], [MIN], [MUL]\n\t")

calc = str(input("Escolha!!\t\t").upper())

if calc == 'SOM':
    result = n1 + n2

elif calc == 'DIV':
    result = n1 + n2

elif calc == 'MIN':
    result = n1 - n2

elif calc == 'MUL':
    result = n1 * n2

print("\n\n\t O Resultado é {}".format(result))























