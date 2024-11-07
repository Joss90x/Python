#Aula 9 Manipulando o texto
# 'Curso em Video python'
# Fatiamento de strings
frase = 'Curso em Video Python'
frase[9:13]
# frase[9:21:2] vai pular de 2 em 2
# frase[:5] vai do inicio até o 5
# frase[15:] vai do 15 até o final
# frase[9::3] vai do 9 até o final pular de 3 em 3

#Análise 
# len(frase) serve para contar quantos caracteres tem na frase 
# frase.count('o') serve para contar quantas vezes aparece a letra o
# frase.count('o', 0, 13) serve para contar quantas vezes aparece a letra o no intervalo de 0 a 13
# frase.find('deo') serve para encontrar a posição onde começa a palavra deo
# frase.find('Android') serve para encontrar a posição onde começa a palavra Android, se não tiver retorna -1
# 'Curso' in frase serve para verificar se a palavra Curso está na frase e vai devolver True ou False

#Transformação
# frase.replace('Python', 'Android') serve para substituir a palavra Python por Android
# frase.upper() serve para deixar a frase toda em maiúscula
# frase.lower() serve para deixar a frase toda em minúscula
# frase.capitalize() serve para deixar a primeira letra maiúscula
# frase.title() serve para deixar a primeira letra de cada palavra maiúscula
# frase.strip() serve para remover os espaços inuteis no começo e no final da frase
# frase.rstrip() serve para remover os espaços inuteis no final da frase
# frase.lstrip() serve para remover os espaços inuteis no começo da frase

#Divisão
# frase.split() serve para dividir a frase em uma lista de palavras
# frase.join() serve para juntar a frase em uma string
# print(''' Texto grande com muitas linhas ''') serve para escrever um texto grande com muitas linhas

