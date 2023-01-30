"""
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
Considere US$1.00 = R$3.27
"""
dinheiro_em_real = float(input('Quanto dinheiro você tem na carteira? R$'))
print(f'Com R${dinheiro_em_real} você pode comprar US${dinheiro_em_real / 3.27:.2f}.')
