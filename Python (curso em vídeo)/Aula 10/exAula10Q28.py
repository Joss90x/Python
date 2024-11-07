# Vamo escrever um programa que faça um pc "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o
#o número escolhido pelo computador. O computador deverá escrever na tela se o usuário venceu. 
from random import randint
from time import sleep
print('-==-' * 20)
print('JOGO DO BARCELOMBRA'.center(80))
print('-==-' * 20)
nome = str(input ('Olá, qual é o seu nome?: '))
numero = randint(0,5)
print(f'{nome} escolhe um número entre 0 e 5')
chute = int(input('Qual número você acha que é?: '))
print('baforando o lança e pensando...')
sleep(3)
print('-==-' * 20)
if chute == numero:
    print(f'{nome} krl bichão, tu acertou!')
else: 
    print('Animal' * 10)
    print(f' muito burro kkkk, eu pensei no número {numero} e não no: {chute}')
    print('Animal' * 10)
print('FIM DO JOGO'.center(80))
print('-==-' * 20)