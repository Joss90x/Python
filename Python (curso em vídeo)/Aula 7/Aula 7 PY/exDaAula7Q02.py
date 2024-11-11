# Vamo criar um algoritmo que leia um número e mostre o dobro, o triplo e a raiz quadrada desse número
n = int(input(' Digite um número: '))
print(f' Dobro: {n*2}\n Triplo: {n*3}\n Raiz quadrada: {n**0.5:.2f}')
 # Coisas que devo fixar no meu cranio:
     # 1. F-string
 #    Para usar uma F-string, coloque a letra 'f' antes das aspas e use chaves {} para inserir variáveis ou expressões dentro da string.
 #    Exemplo:
 #    nome = "Maria"
 #    idade = 30
 #    print(f"Olá, meu nome é {nome} e tenho {idade} anos.")
 #    Isso imprimirá: "Olá, meu nome é Maria e tenho 30 anos."
 #    Imagine que você tem uma caixinha mágica chamada F-string.
 #    Essa caixinha é muito especial porque ela pode guardar palavras e números juntos!
 #    É como se você pudesse colocar um brinquedo e um número na mesma caixinha.
 #    Por exemplo, se você quiser dizer "Eu tenho 5 anos", a F-string ajuda você a fazer isso facilmente.
 #   É como se fosse um truque de mágica para misturar palavras e números de um jeito bem legal!

    # 2. \n para quebrar linha ou como o Guanabara disse: "nova linha"

    # 3. :.2f é como uma mágica que faz os números ficarem mais bonitinhos!
 #    Imagine que você tem um número grande com muitos números depois da vírgula,
 #    tipo 3,14159265... Essa mágica faz com que só apareçam dois números depois da vírgula,
 #    então fica 3,14. É como se estivéssemos arredondando o número para ficar mais fácil de ler! 