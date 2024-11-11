#Vamo escreverum programa que leia um número inteiro qualquer e pedir para o usúario escolher qual vai ser a base de conversão
#1. Binário
#2. octal
#3. hexadecimal
número = int(input('DIgite um número inteiro: '))
print('''Escolha uma das bases para a conversão:
[1] Converter para o BINÁRIO
[2] Converter para o OCTAL
[3] Converter para o HEXADECIMAL''')
opção = int(input('Qual você quer?: '))
if opção == 1:
    print(f'O número {número} é {bin(número)[2:]} em binário')
elif opção == 2:
    print(f'O numero {número} é {oct(número)[2:]} em OCTAL')
elif opção == 3:
    print(f'O número {número} é {hex(número)[2:]} em HEXADECIMAL')
else:
    print('Opção invalida burrão')