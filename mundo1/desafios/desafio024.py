"""
Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".
"""
nome_da_cidade = input('Digite o nome de sua cidade: ').upper()
if nome_da_cidade.split()[0] == "SANTO":
    print(f'A cidade {nome_da_cidade.title()} possui SANTO no começo do nome.')
else:
    print(f'A cidade {nome_da_cidade.title()} não possui SANTO no começo do nome.')