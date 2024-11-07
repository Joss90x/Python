print('-==-' * 20)
print('Analisador de triângulos')
s1 = float(input('Qual é o primeiro seguimento?: '))
s2 = float(input('Qual é o segundo seguimento?: '))
s3 = float(input('Qual é o terceiro seguimento?: '))
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('Os segmentos acima PODEM FORMAR um triângulo! ')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo!')
print('-==-' * 20)
