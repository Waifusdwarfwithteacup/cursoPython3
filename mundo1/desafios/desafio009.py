"""
Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.
"""
número_digitado = int(input('Digite um número para ver sua tabuada: '))
contador = 1
while contador <= 10:
    print(f'[{número_digitado:2}] X [{contador:2}] = {número_digitado * contador:2}.')
    contador+=1

