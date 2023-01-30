"""
Crie um programa que leia um número inteiro qualquer e mostre na sua tela se ele é PAR ou ÍMPAR.
"""
número_digitado = int(input('Digite um número: '))
if número_digitado%2 == 0:
    print(f'O número {número_digitado} é PAR.')
else:
    print(f'O número {número_digitado} é ÍMPAR.')
