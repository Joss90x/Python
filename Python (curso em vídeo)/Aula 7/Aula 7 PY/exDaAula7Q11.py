#Vamos criar um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade 
# de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².
# Eu não escrevi nada do que foi pedido e essa porra apareceu de sugestão perfeitamente como ta no video do professsor 
# sinistro.
Largura = float(input('Qual a largura da parede?'))
Altura = float(input('Qual a altura da parede?'))
Area = Largura * Altura 
tinta = Area / 2
print(f'Para pintar a parede, você precisará de {tinta} litros de tinta')





