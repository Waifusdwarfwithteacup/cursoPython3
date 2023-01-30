"""
Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo
e todas as informações possíveis sobre ele.
"""
valor_aleatório = input('Digite algo: ')
print(f'O tipo primitivo de {valor_aleatório} é [{type(valor_aleatório)}].')
print(f'Possui apenas espaços? [{valor_aleatório.isspace()}].')
print(f'É um número? [{valor_aleatório.isnumeric()}].')
print(f'É alfabético? [{valor_aleatório.isalpha()}].')
print(f'É alfanúmerico? [{valor_aleatório.isalnum()}].')
print(f'Está apenas em maiúsculas? [{valor_aleatório.isupper()}].')
print(f'Está apenas em minúsculas? [{valor_aleatório.islower()}].')
print(f'Está capitalizada? [{valor_aleatório.istitle()}].')

