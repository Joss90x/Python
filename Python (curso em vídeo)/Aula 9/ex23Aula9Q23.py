# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados.
#num = int(input('Digite um número'))
#n = str(num)
#print(f'Analisando o número {num}')
#print(f'Unidade: {}')
num = int(input('Digite um número: '))
u = num // 1 % 10
d = num // 10 % 10  
c = num // 100 % 10
m = num // 1000 % 10
print(f'Analisando o número {num}')
print(f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'Centena: {c}') 
print(f'Milhar: {m}')
"""
Este programa lê um número inteiro de 0 a 9999 e separa cada dígito, mostrando:

- A unidade (último dígito)
- A dezena (penúltimo dígito) 
- A centena (antepenúltimo dígito)
- O milhar (primeiro dígito)

Para fazer isso, o programa usa divisão inteira (//) e resto da divisão (%) da seguinte forma:

- unidade = num // 1 % 10    -> Divide por 1 e pega o resto por 10
- dezena = num // 10 % 10    -> Divide por 10 e pega o resto por 10  
- centena = num // 100 % 10  -> Divide por 100 e pega o resto por 10
- milhar = num // 1000 % 10  -> Divide por 1000 e pega o resto por 10

Exemplo:
Para o número 1234:
- 1234 // 1 = 1234 -> 1234 % 10 = 4 (unidade)
- 1234 // 10 = 123 -> 123 % 10 = 3 (dezena)
- 1234 // 100 = 12 -> 12 % 10 = 2 (centena)
- 1234 // 1000 = 1 -> 1 % 10 = 1 (milhar)
"""




          