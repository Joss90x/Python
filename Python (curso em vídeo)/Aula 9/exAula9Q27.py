
#faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
nome = str(input('digite seu nome completo:')).strip()
n2 = nome.split()
print('Oii')
print(f'seu primeiro nome é {n2[0]}')
print(f'seu último nome é {n2[-1]}')


