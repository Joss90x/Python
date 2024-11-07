# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salario = float(input('Qual é o salário do funcionário?'))
ns = salario + (salario * 15/100)
print(f'O salário do funcionário com aumento de 15% fica: {ns}')
