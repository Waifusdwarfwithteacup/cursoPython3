"""
Faça um algorimo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
"""
salário_funcionário = float(input('Qual é o seu salário? R$'))
print(f'Um funcionário(a) que ganhava R${salário_funcionário}, com 15% de aumento, passa a receber R${(((salário_funcionário * 15)/100)+ salário_funcionário):.2f}.')
