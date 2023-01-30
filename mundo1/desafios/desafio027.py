"""
Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
Ex:
Ana Maria de Souza
Primeiro: Ana
último: Sousa
"""
nome_completo = input('Digite o seu nome completo: ')
print(f'Primeiro nome: {nome_completo.split()[0]}, último nome: {nome_completo.split()[-1]}.')
