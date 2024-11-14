#Vamo desenvolver uma logica que leia o peso e a altura de uma pessoa e 
# calcule o IMC E mostre seu status, de acordo com a tabela abaixo:
# IMC abaixo de 18,5: Abaixo do peso
# IMC entre 18,5 e 25: Peso ideal
# IMC entre 25 e 30: Sobrepeso
# IMC acima de 30: Obesidade
peso = float(input('Qual é o seu peso?: '))
altura = float(input('Qual é a sua altura?: '))
imc = peso / (altura ** 2)
if imc  < 18.5:
    print(f'Seu IMC é {imc:.2f} e você está abaixo do peso')
elif imc >= 18.5 and imc < 25:
    print(f'Seu IMC é {imc:.2f} e você está no peso ideal.')
elif imc >= 25 and imc < 30:
    print(f'Seu IMC é {imc:.2f} e vocé esta com sobrepeso')
elif imc >= 30 and imc < 40:
    print(f'Seu IMC é {imc:.2f} e vocé esta com obesidade')
else:
    print(f'Seu IMC é {imc:.2f} e vocé esta com obesidade morbida')