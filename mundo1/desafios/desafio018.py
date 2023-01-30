"""
Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
"""
from math import sin, cos, tan, radians
ângulo_digitado = int(input('Digite um ângulo: '))
print(f'O valor do seno é: {sin(radians(ângulo_digitado)):.2f}.')
print(f'O valor do cosseno é: {cos(radians(ângulo_digitado)):.2f}.')
print(f'O valor da tangente é: {tan(radians(ângulo_digitado)):.2f}.')
