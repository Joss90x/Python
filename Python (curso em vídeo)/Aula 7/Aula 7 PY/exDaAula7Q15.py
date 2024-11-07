#Excreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos
#quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por km rodado.
alg = float(input('Qual é o valor do aluguel?' ))
km = float(input('Quantos km você rodou?' ))
dias = int(input('Quantos dias você ficou com o carro?' ))
pagar = (alg * dias) + (km *0.15)
print(f'Você terá que pagar R${pagar:.2f}')
#esse foi mais de boa de fazer e eu usei pouco a ajuda do cursor, mas eu acho que vou usar isso na minha vida

