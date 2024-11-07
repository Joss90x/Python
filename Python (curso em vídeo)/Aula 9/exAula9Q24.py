# Faça um programa que leia a palavra santo
cidade = str(input('Em que cidade você nasceu? ')).strip()
print(cidade[:5].upper() == 'SANTO')
"""
Este programa verifica se uma cidade começa com a palavra 'SANTO'. Aqui está como ele funciona:

1. Primeiro pede ao usuário para digitar o nome da cidade onde nasceu
   cidade = str(input('Em que cidade você nasceu? ')).strip()

2. O .strip() remove espaços em branco no início e fim do texto

3. cidade[:5] pega os 5 primeiros caracteres da string
   
4. .upper() converte esses caracteres para maiúsculas

5. Compara se esses 5 caracteres são iguais a 'SANTO'
   
6. Retorna True se a cidade começar com 'SANTO' e False caso contrário

Por exemplo:
- "Santo André" -> True 
- "santos" -> False
- "SANTO AMARO" -> True
- "São Paulo" -> False
"""
