"""
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1.250.00, calcule um aumento de 10%.
Para salários inferiores ou iguais, o aumento é de 15%.
"""
salário = float(input('Digite o seu salário: '))
if salário<=1250:
    print(f'O seu salário era R${salário} com o aumento de 15%, agora é de R${salário + ((salário * 15) / 100):.2f}.')
else:
    print(f'O seu salário era R${salário} com o aumento de 10%, agora é de R${salário + ((salário * 10)/100):.2f}.')
