# Programa para mostrar o sucessor e antecessor de um número inteiro
# Lê um número inteiro do usuário
# Esta linha solicita ao usuário que digite um número inteiro
# A função input() exibe a mensagem e espera que o usuário digite algo
# O valor digitado é convertido para um número inteiro usando int()
# O resultado é armazenado na variável 'numero'
n = int(input("Digite um número inteiro: "))

# Calcula o antecessor e o sucessor
# Esta linha calcula o antecessor do número digitado
# Subtrai 1 do valor armazenado na variável 'numero'
# O resultado é armazenado na variável 'antecessor'
antecessor = n - 1
sucessor = n + 1

# Mostra os resultados na tela
print(f"O antecessor de {n} é {antecessor}")
print(f"O sucessor de {n} é {sucessor}")
