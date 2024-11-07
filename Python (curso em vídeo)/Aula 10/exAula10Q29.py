speed = float(input('Qual a velocidade do seu carro?: '))
if speed > 80: 
    print('Anda devagar fela da puta!')
    print(f'leva pra casa um presente de {(speed - 80) * 7:.2f} Reais')
else:
    print('Ta de boa corno, mantém a mesma velocidade!')
