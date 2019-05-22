"""

Criar um logaritmo que insera 4 notas e nome do aluno.
0 - 4 ~ reprovado
4 - 7 ~ recuperação
7 - 8 ~ aprovado
9 - 10 ~ aprovado com louvor

O Código deve realizar a criação de uma prova com cinco. perguntas (para simular escrevar qualquer coisa que tenha
resposta sim ou nao, cada pergunta pode ter duas respostas.
Se o Aluno escolher sim o questionario deve somar 2 pontos.
O Aluno, caso contrario nao deve somar, ao final o sistema deve mostrar o total da nota alcanda pelo aluno

"""

nm = input("Digite o nome do Aluno: ").title()
nt1 = float(input("Digite a nota do primeiro Bimestre: "))
nt2 = float(input("Digite a nota do segundo Bimestre: "))
nt3 = float(input("Digite a nota do terceiro Bimestre: "))
nt4 = float(input("Digite a nota do quarto Bimestre: "))

media = (nt1 + nt2 + nt3 + nt4) / 4

if media <= 4.0:
    print("A média do Aluno {} é {:.1f}, ele se encontra REPROVADO!!".format(nm, media))

elif 4.1 >= media < 6.9:
    print("A média do Aluno {} é {:.1f}, ele esta de Recuperação!!".format(nm, media))

elif 7.0 >= media <= 8.9:
    print("A média do Aluno {} é {:.1f}, ele esta Aprovado!!".format(nm, media))

elif media >= 9.0:
    print("A média do Aluno {} é {:.1f}, ele esta Aprovado com LOUVOR!!".format(nm, media))
