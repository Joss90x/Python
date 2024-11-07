# 1. O "import " serve pra tipo a todos os itens que estão dentro do arquivo
# Um exemplo é o "math" que tem várias funções matemáticas que são: ceil, floor, trunc, pow, sqrt, factorial, etc.
# Pra usar é simples: import math e depois é só usar a função que eu quero, mas tem que usar o math.nomedafunção

# 2.O "from" já é pra ser usado pra quando eu quiser importar apenas um ítem específico
# agora se eu quero usar apenas uma função específica, eu uso o from: from math import pow

#import math, random 
#num = int(input('Digite um número:'))
#raiz = math.sqrt(num)
#print(f'A raiz de {num} é igual a {raiz:.2f}')

# Quando eu usar "from math import sqrt", eu não preciso usar o "math.sqrt" pode ser só "sqrt"
# também posso usar o "from math import sqrt, floor" ai vou poder usar essas duas funçoes sem precisar usar tudo do math  
# EX. import msth sqrt, floor

#import random 
#num = random.randint(1,100)
#print(f'teu pau é desse tamanho: {num}cm')
import emoji
# Para instalar o pacote emoji, abra o terminal e digite:
# pip install emoji

# Depois de instalado, você pode usar assim:
print(emoji.emojize('Python is :thumbs_up:'))
print(emoji.emojize('Olá, Mundo! :earth_americas:', language='alias'))
print(emoji.emojize('krl :rage:'))
print(emoji.emojize('euuu :grinning_face:'))


# Se ainda não funcionar, tente reinstalar:
# pip uninstall emoji
# pip install emoji

# Ou atualize o pip:
# python -m pip install --upgrade pip

