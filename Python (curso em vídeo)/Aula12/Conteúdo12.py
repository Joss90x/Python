# O conteúdo da aula 12 é condições alinhadas 
nome = str(input('Qual é o seu nome?'))
if nome == 'Joss':
    print('É você picudo?')
elif nome == 'Kaleby' or nome == 'cabra' or nome == 'andrey':
    print('Que nome de gente baixa')
elif nome == 'Jeandra':
    print('Amor da minha vida')
else:
    print('Que nome normal')
    print(f'fica de boa ai {nome}')