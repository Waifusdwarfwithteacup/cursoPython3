"""
Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
"""
distância_em_metros = int(input('Digite uma distância em metros: '))
print(f'A medida de {distância_em_metros} corresponde a: ')
print(f'{distância_em_metros / 1000}km.')
print(f'{distância_em_metros / 100}hm.')
print(f'{distância_em_metros / 10}dam.')
print(f'{distância_em_metros * 10}dm.')
print(f'{distância_em_metros * 100}cm.')
print(f'{distância_em_metros * 1000}mm.')

