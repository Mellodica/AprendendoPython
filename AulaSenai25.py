







print("\n DIGITE SUA PRIMEIRA PERGUNTA:\n\t")
pr1 = str(input("\n").upper())


print("\n DIGITE SUA SEGUNDA PERGUNTA! VALENDOOOOOO!\n\t")
pr2 = str(input("\n").upper())


print("\nDIGITE SUA TERCEIRA PERGUNTA!\n\t")
pr3 = str(input("\n").upper())

print("\n\n\n\n\t\t   VALEEEEENDOOOOO!")
print(pr1+'\n\n')
pr01 = str(input("***** Digite [SIM] ou [NAO] *****\n\t\t").upper())

if pr01 == 'SIM':
    r1 = 2
else:
    r1 = 0


print("\n PERGUNTA DOIS!")
print(pr2+'\n\n')
pr02 = str(input("***** Digite [SIM] ou [NAO] *****\n\t\t").upper())

if pr02 == 'SIM':
    r2 = 2
else:
    r2 = 0


print("\n PERGUNTA TRÊS!!")
print(pr3+'\n\n')
pr03 = str(input("***** Digite [SIM] ou [NAO] *****\n\t\t").upper())

if pr03 == 'NAO':
    r3 = 2
else:
    r3 = 0


soma = r3 + r1 + r2



print("\n\n\n Cada Pergunta tem o Valor de 2 Pontos sua pontuação foi {}".format( soma))
















