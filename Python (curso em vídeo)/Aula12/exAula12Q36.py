#vamo fazer um programa para aprovar um empréstimo bancário para a compra de uma casa o programa vai perguntar o valor da casa 
# o salário do comprador e em quantos anos ele vai pagar ]
import emoji
print('-==-' * 20)
print(emoji.emojize(':eggplant:Empréstimo pica:eggplant:'.center(80))) 
print('-==-' * 20)
casa = float(input('Qual o valor da casa?:$')) 
salario = float(input('Qual é o seu salário?:$'))
anos = int(input('Quantos anos você vai pagar?:' ))
prestação = casa / (anos * 12)
minimo = salario * 30/100
if prestação <= minimo:
    print(f'Parabéns! você foi aprovado! A prestação mensal é de {prestação:.2f}')
else:
    print('O valor foi negado seu merda, pq passou dos 30%')