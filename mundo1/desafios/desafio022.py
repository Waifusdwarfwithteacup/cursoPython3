"""
Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas.
- O nome com todas as minúsculas.
- Quantas letras ao todo(sem considerar espaços).
- Quantas letras tem o primeiro nome.
"""
nome_completo = input('Digite o seu nome completo: ').strip()
print(f'O seu nome com todas as letras maiúsculas: {nome_completo.upper()}.')
print(f'O seu nome com todas as letras minúsculas: {nome_completo.lower()}.')
print(f'O seu nome é assim sem espaços: {nome_completo.replace(" ","")} e possui {len(nome_completo.replace(" ",""))} letras.')
print(f'O seu primeiro nome é {nome_completo.split()[0]} e possui {len(nome_completo.split()[0])} letras.')

