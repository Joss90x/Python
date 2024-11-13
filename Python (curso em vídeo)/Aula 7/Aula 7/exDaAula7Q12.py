# Vamos fazer um algoritmo que leia o preço de um kimono e mostre seu novo preço, com 5% de desconto.
preco = float(input('Qual é o preço do kimono da kings?: '))
np = preco - (preco * 5/100)
print(f' O preço do kimono com desconto de 5% fica por: {np}')
