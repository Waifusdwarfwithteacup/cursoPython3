"""
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo,
calcule e mostre o comprimento da hipotenusa.
"""
from math import pow, sqrt, trunc
cateto_oposto = int(input('Digite o cateto oposto: '))
cateto_adjacente = int(input('Digite o cateto adjacente: '))
print(f'X² = {cateto_oposto}² + {cateto_adjacente}², o comprimento da hipotenusa é igual à: {trunc(sqrt((pow(cateto_oposto, 2) + (pow(cateto_adjacente, 2)))))}cm.')
