"""
Desenvolva um programa que leia o comprimento de três retas, diga ao usuário se elas podem ou não formar um triângulo.
"""
primeira_reta = int(input('Digite a 1ª reta: '))
segunda_reta = int(input('Digite  a 2ª reta: '))
terceira_reta = int(input('Digite a 3ª reta: '))
if primeira_reta + segunda_reta > terceira_reta and primeira_reta + terceira_reta > segunda_reta and segunda_reta + terceira_reta > primeira_reta:
    print(f'Pode formar um triângulo!')
else:
    print(f'Não pode formar um triângulo!')
