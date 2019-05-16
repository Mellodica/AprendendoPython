

while True:
    stringDigitada = input('Digite uma palavra: ')
    if stringDigitada.lower()=='sair':
        print('Fim!')
        break

    if len(stringDigitada) < 2:
        print('String muito Pequena!')
        print('Tente digitar sair!')
        continue

