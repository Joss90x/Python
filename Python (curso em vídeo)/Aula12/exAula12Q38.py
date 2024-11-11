#vamo fazer um programa que leis números inteiros e compares-os mostrando na tela uma mensagem:
# O primeiro valor é maior
# o segundo valor é maior
# não existe valor maior, os dois são iguais
num = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
if num > num2:
    print(f'O primero valor {num} é maior')
elif num2 > num:
    print(f'O segundo valor é maior' )
# Start of Selection
else:
    print('Não existe valor maior, os dois são iguais.')
