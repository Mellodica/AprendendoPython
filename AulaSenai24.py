"""
O Código deve realizar a criação de uma prova com cinco. perguntas (para simular escrevar qualquer coisa que tenha
resposta sim ou nao, cada pergunta pode ter duas respostas.
Se o Aluno escolher sim o questionario deve somar 2 pontos.
O Aluno, caso contrario nao deve somar, ao final o sistema deve mostrar o total da nota alcanda pelo aluno
"""




nm = input("Digite o nome do Aluno: ").title()

print("\nA Capital do Paraná é CURITIBA?")
pr1 = str(input("\n***** Digite [SIM] ou [NAO] *****\n\t\t").upper())
if pr1 == 'SIM':
    r1 = 2
else:
    r1 = 0
print("\n SEGUNDA PERGUNTA! VALENDOOOOOO!")
print("\nUma pais da Europa! Essa Frase foi dita pelo FAUSTAO?")
pr2 = str(input("***** Digite [SIM] ou [NAO] *****\n\t\t").upper())
if pr2 == 'SIM':
    r2 = 2
else:
    r2 = 0


print("\n TERCEIRA PERGUNTA!!! VALENDOOOOO!!!")
print("\nTá pegando Fogo Bicho! - Essa frase foi dita pelo Gugu?")
pr3 = str(input("***** Digite [SIM] ou [NAO] *****\n\t\t").upper())
if pr3 == 'NAO':
    r3 = 2
else:
    r3 = 0

print("\nQuarta pergunta! VALEEEEENDOOOOO!")
print("\nA Turma B de TDS, é a melhor do Portão?")
pr4 = str(input("***** Digite [SIM] ou [NAO] *****\n\t\t").upper())
if pr4 == 'NAO':
    r4 = 2
else:
    r4 = 0

soma = r1+r2+r3+r4

print("\n\nOlá {}. A Soma da Pontuação é {}".format(nm, soma))






















