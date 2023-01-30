"""
Escreva um programa que faça o computador 'pensar' em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir
qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu!
"""
from random import randint
número_pensado_pelo_computador = randint(0,5)
número_digitado = int(input('Eu pensei em um número entre 0 e 5, digite qual número pensei: '))
if número_digitado <=5 and número_digitado >=0:
    if número_pensado_pelo_computador == número_digitado:
        print(f'Eu pensei no número {número_pensado_pelo_computador} e você digitou {número_digitado}, meus parabéns, você acertou!')
    else:
        print(f'Eu pensei no número {número_pensado_pelo_computador} e você digitou {número_digitado}, infelizmente você errou! Tente novamente.')
else:
    print(f'O valor {número_digitado} infelizmente não é válido! Tente novamente.')
