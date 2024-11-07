from random import choice
morte = str(input('Quem é que vai morrer primeiro? digita aqui o nome: '))
morte2 = str(input('Quem é o outro?' ))
morte3 = str(input('Quem é o terceiro?' ))
lista = [morte,morte2,morte3]
print(f' O sortudo foi o {choice(lista)}')
