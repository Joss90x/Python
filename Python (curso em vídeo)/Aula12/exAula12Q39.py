#vamo fzer um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar
# ao servoço militar, se é a hora de se alistar ou se já passou do tempo do alistamento. seu programa também deverá mostra o tempo 
# que falta ou que passou do prazo.
from datetime import datetime
nascimento = int(input('Qual ano você nasceu?: '))
ano_atual = datetime.now().year
idade = ano_atual - nascimento 
if idade < 18:
    print(f'você tem {idade} anos e ainda falta {18 - idade} anos para se alistar')
elif idade == 18:
    print(f'Chegou a hora de se alistar ao exército brasileiro')
else:
    print(f'Passou do tempo de alistamento já pq vc já tem {idade} anos. ')
