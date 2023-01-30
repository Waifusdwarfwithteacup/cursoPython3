"""
Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
"""
from math import sqrt
número_digitado = int(input('Digite um número: '))
print(f'O Dobro de {número_digitado} vale {número_digitado * 2}.')
print(f'O triplo de {número_digitado} vale {número_digitado * 3}.')
print(f'A raiz quadrada de {número_digitado} é igual a {sqrt(número_digitado):.2f}.')
