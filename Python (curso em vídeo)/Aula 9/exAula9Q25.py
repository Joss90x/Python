# Vamo fazer um programa que leia o nome completo de uma pessoa e ver se tem silva no nome
nome = str(input('Qual é o seu nome seu lindo?')).strip()
print(f'Seu nome tem Silva? {"SILVA" in nome.upper()}')
"""
Este programa verifica se uma pessoa tem 'Silva' em seu nome. Aqui está como ele funciona:

1. Primeiro pede ao usuário para digitar seu nome completo
   nome = str(input('Qual é o seu nome seu lindo?')).strip()

2. O .strip() remove espaços em branco no início e fim do texto

3. nome.upper() converte todo o nome para maiúsculas para fazer uma comparação 
   sem diferenciar maiúsculas/minúsculas

4. O operador 'in' é usado para verificar se um valor está contido em outro.
   Neste caso, "SILVA" in nome.upper() verifica se a palavra "SILVA" está 
   contida no nome convertido para maiúsculas.
   
   O operador 'in' retorna:
   - True: se encontrar o valor procurado
   - False: se não encontrar

5. Retorna True se encontrar "SILVA" em qualquer parte do nome e False caso contrário

Por exemplo:
- "José Silva Santos" -> True
- "Maria da Silva" -> True 
- "João Santos" -> False
- "Pedro silva oliveira" -> True (mesmo em minúsculo)

O operador 'in' é muito útil para:
- Verificar se um elemento está em uma lista
- Verificar se uma string contém outra string
- Verificar se uma chave existe em um dicionário
"""


