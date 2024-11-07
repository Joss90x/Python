dist = float(input('Qual a distância da sua viagem?: '))
if dist <= 200:
    print(f'O valor da sua passagem será de R${dist * 0.50:.2f}')
else:
    print(f'O valor da sua passagem será de R${dist * 0.45:.2f}')