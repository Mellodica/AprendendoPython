'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

Programa que leia três números e mostre o maior deles.

Programa que leia três números e mostre o maior e o menor deles.

Programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

Programa que leia três números e mostre-os em ordem decrescente.

'''
'''
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))

if num1 > num2 and num3:
    print(num1)
    
elif num2 > num1 and num3:
    print(num2)

elif num3 > num1 and num2:
    print(num3)

'''
'''
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))

if num1 > num2 and num3:
    if num2 > num3:
        print('O maior número é o {} e o menor é {}'.format(num1, num3))
    
    if num3 > num2:
        print('O maior valor é {} e o menor valor é {}'.format(num1, num2))
    
    
elif num2 > num1 and num3:
    if num1 > num3:
        print('O maior número é o {} e o menor é {}'.format(num2, num3))
    
    if num3 > num1:
        print('O maior valor é {} e o menor valor é {}'.format(num2, num1))

elif num3 > num1 and num2:
    if num2 > num1:
        print('O maior número é o {} e o menor é {}'.format(num3, num1))
    
    if num1 > num2:
        print('O maior valor é {} e o menor valor é {}'.format(num3, num2))
'''

'''
num1 = float(input('Digite o primeiro preço: '))
num2 = float(input('Digite o segundo preço: '))
num3 = float(input('Digite o terceiro preço: '))

if num1 < num2 and num3:
    print('O menor valor é {}'.format(num1))
    
elif num2 < num1 and num3:
    print('O menor valor é {}'.format(num2))
    
elif num3 < num1 and num2:
    print('O menor valor é {}'.format(num3))

'''
'''
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))


if num1 > num2 and num3:
    if num2 > num3:
        print('A ordem decrescente é {}, {}, {}'.format(num1, num2, num3))
       
    if num3 > num2:
        print('A ordem decrescente é {}, {}, {}'.format(num1, num3, num2))
    
    
elif num2 > num1 and num3:
    if num1 > num3:
        print('A ordem decrescente é {}, {}, {}'.format(num2, num1, num3))
    
    if num3 > num1:
        print('A ordem decrescente é {}, {}, {}'.format(num2, num3, num1))

elif num3 > num1 and num2:
    if num2 > num1:
        print('A ordem decrescente é {}, {}, {}'.format(num3, num2, num1))
    
    if num1 > num2:
        print('A ordem decrescente é {}, {}, {}'.format(num3, num1, num2))
        
        
  '''
  
  
        
        
        
        
        