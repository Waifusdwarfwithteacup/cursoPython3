"""
Faça um programa que leia a largura e a altura de uma parede em metros,
calcule a sua área e a quantidade de tinta nescessária para pintá-la, sabendo que cada litro de tinta,
pinta uma área de 2m².
"""
largura_da_parede = float(input('Largura da parede: '))
altura_da_parede = float(input('Altura da parede: '))
print(f'Sua parede tem a dimensão de {largura_da_parede}X{altura_da_parede} e sua área é de {largura_da_parede*altura_da_parede}m².')
print(f'Para pintar essa parede, você precisará de {(largura_da_parede * altura_da_parede)/2:.2f}l de tinta.')
