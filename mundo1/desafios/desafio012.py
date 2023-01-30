"""
Faça um algortimo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
"""
preço_do_produto = float(input('Qual é o preço do produto? R$'))
print(f'O produto que custava R${preço_do_produto}, na promoção com desconto de 5% vai custar R${(preço_do_produto - ((preço_do_produto * 5) / 100)):.2f}')
