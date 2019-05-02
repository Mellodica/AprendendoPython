# Cadeia de Caracteres
#Aula Numero 09

#String ou Cadeia de Caracteres

frase = 'Curso em Video Python'

#Fatiamento

#Mostra a Letra que esta no campo 9
print(frase[9])

#Mostra as Letras entre o Campo 9 ao 14
print(frase[9:14])

print(frase[9:21])

print(frase[9:21:2])

#Não colocar valor no primeiro Operador é identificado como ZERO
print(frase[:5])

#A Operação vai até o final da rede de string
print(frase[15:0])

print(frase[9::3])

#Analise

#Operador LEN
#Identifica quantos caracteres existe na FRASE
print(len(frase))

#Operador COUNT
#Conta quantas vezes uma determinada LETRA aparece
print(frase.count('o'))
#incluindo fatiamento
print(frase.count('o', 0, 13))

#Operador FIND
#Encontra Inicio de determinada Letra ou Letras
print(frase.find('deo'))

#Operador IN
#Ira Validar entre TRUE ou FALSE
print('Curso' in frase)

#Transformação
#Operador REPLACE
print(frase.replace('Python', 'Android'))

#UPPER() - Metodo
#Deixar letras maiusculas
print(frase.upper())

#LOWER - Metodo
#Deixa tudo em Minusculo
print(frase.lower())

#Capitalize()
#Deixa todas as Primeiras Letras em Maiusculas
print(frase.capitalize())

#TITTLE()
#Deixa a primeira letra Maiuscula, mas identificando cadas letra
print(frase.title())

app = '   Aprenda Python   '

#STRIP()
#O Metodo Strip remove todos os espaço do inicio e do final de uma String\Frase
print(app.strip())

#rstrip remove os espaços do lado direito
#lstrip remove os espaços do lado esquerdo

#DIVIDIR \ DIVISÃO

#SPLIT()
#O Metodo split pega os espaço de uma frase e divide
#cada Palavra dentro de uma frase acaba recendo uma numeracao nova fazendo cada frase uma lista

print(frase.split())

#JUNÇÃO \ UNIAO

#'-'.JOIN()
print('-'.join(frase))
