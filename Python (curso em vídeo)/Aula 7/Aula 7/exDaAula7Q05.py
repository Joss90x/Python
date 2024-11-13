#Vamo fazer uma tabuada de um número qualquer.
numero = int(input('Digite um número para a tabuada:'))
print('-' * 12)
print(f'Tabuada do número {numero}:')
print(f'{numero} x 1 = {numero *1}')
print(f'{numero} x 2 = {numero *2}')
print(f'{numero} x 3 = {numero *3}')
print(f'{numero} x 4 = {numero *4}')
print(f'{numero} x 5 = {numero *5}')
print(f'{numero} x 6 = {numero *6}')
print(f'{numero} x 7 = {numero *7}')
print(f'{numero} x 8 = {numero *8}')
print(f'{numero} x 9 = {numero *9}')
print(f'{numero} x 10 = {numero *10}')
print('-' * 12)
# Explicação do código:

# Este programa cria uma tabuada simples para um número escolhido pelo usuário.

# 1. Entrada de dados:
#    A linha `numero = int(input('Digite um número para a tabuada:'))` pede ao usuário
#    que digite um número e o converte para inteiro. Este será o número base da tabuada.

# 2. Exibição do cabeçalho:
#    `print(f'Tabuada do número {numero}:')` mostra um título para a tabuada,
#    indicando qual número será multiplicado.

# 3. Cálculo e exibição da tabuada:
#    As linhas seguintes usam f-strings para mostrar as multiplicações de 1 a 10.
#    Por exemplo: `print(f'{numero} x 1 = {numero *1}')`
#    Isso multiplica o número escolhido por 1 e mostra o resultado.
#    O processo se repete até 10.

# 4. Formatação:
#    O uso de f-strings (f'...') permite inserir variáveis e expressões diretamente
#    na string, tornando o código mais legível e fácil de entender.

# 5. Simplicidade:
#    Este código é direto e eficiente para criar uma tabuada básica.
#    Para uma versão mais avançada, poderíamos usar um loop 'for' para
#    reduzir a repetição de código.

# Dica:
# Para praticar, tente reescrever este programa usando um loop 'for'.
# Isso tornará o código mais curto e flexível!


