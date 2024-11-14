#Vamo criar um programa que leia o ano de nascimento de um atleta
# e mostre sua categoria, de acordo com a idade:
from datetime import datetime
nascimento = int(input('Qual ano você nasceu?: '))
ano_atual = datetime.now().year 
idade = ano_atual - nascimento
if idade <= 15:
    print(f'Você tem {idade} e sua categoria é KIDS!')
elif idade  <= 17:
    print(f'Você tem {idade} e sua categoria é JUVENIL!')
elif idade <=29:
    print(f'Você tem {idade} e sua categoria é ADULTO!')
else:
    print(f'Você tem {idade} e sua categoria é MASTER!')
''