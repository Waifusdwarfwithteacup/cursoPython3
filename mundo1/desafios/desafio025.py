"""
Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
"""
nome_da_pessoa = input('Digite seu nome: ').upper()
resultado = "SILVA" in nome_da_pessoa
if resultado == True:
    print(f'O nome {nome_da_pessoa.title()} possui Silva no nome.')
else:
    print(f'O nome {nome_da_pessoa.title()} não possui Silva no nome.')

