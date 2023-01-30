"""
Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.
"""
import workadays.workdays
ano_digitado = int(input('Digite um ano qualquer: '))
ano_bissexto = workadays.workdays.is_leap_year(ano_digitado)
if ano_bissexto == True:
    print(f'O ano de {ano_digitado} é Bissexto!')
else:
    print(f'O ano de {ano_digitado} não é Bissexto!')


