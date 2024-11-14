#refaça o desafio 035 dos triângulos, acrescentando o recurso de mortrar o
#tió do de triângulo será na formado:
#Equilatero - todos os lados iguais 
#Isosceles - dois lados iguais
#Escaleno - todos os Lados diferentes

l1 = float(input('Primeiro lado do triângulo: '))
l2 = float(input('Segundo lado do triângulo: '))
l3 = float(input('Terceiro lado do triângulo: '))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('Os segmentos acima PODEM FORMAR um triângulo! ')
    if l1 == l2 == l3:
        print('Todos os lados iguais logo o triângulo será EQUILATERO.')
    elif l1 == l2 or  l2 == l3 or l3== l1:
        print('Dois lados iguais Logo o triângulo será ISÓSCELES.')
    else:
        print('Todos os lados diferentes logo o triângulo é ESCALENO.')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo!')
    #essa aqui eu bati cabeça pra fazer
