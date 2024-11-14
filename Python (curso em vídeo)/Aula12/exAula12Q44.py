print(f'{' LOJA DO JOSS ':=^40}')
preço = float(input('Qual é o preço do iphone? R$:'))
print('''Forma de pagamento:
[1] A vista dinheiro ou pix (10% de desconto)
[2] A vista no cartão(5% de desconto)
[3] Parcelado em 2x
[4] Parcelado em 3x ou mais (20% de Juros)''')
opção = int(input('Qual é a opção de pagamento?: '))
if opção == 1:
    print(f'O iphone ficará por {preço - (preço * 10/100)}')
elif opção == 2:
    print(f'O iphone ficará por {preço - (preço * 5/100)} ')
elif opção == 3:
    print(f'O iphone ficará por {preço}')
elif opção == 4:
    total = preço + (preço * 20/100)
    parcelas= int(input(f'Quantas vezes você desejar parcelar?: '))
    print(f'O iphone que custa ${preço:.2f} de {parcelas}X ficará por ${total:.2f}')
else:
    total = 0 
    print('Opção invalida de pagamento. Tente novamente :)')