"""
Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens até 200Km e R$0,45 para viagens mais longas.
"""
distância_em_km = int(input('Digite a distância que vai percorrer na sua viagem: '))
if distância_em_km <=200:
    print(f'O valor da sua passagem é R${distância_em_km * 0.50:.2f}.')
else:
    print(f'O valor da sua passagem é R${distância_em_km * 0.45:.2f}.')
