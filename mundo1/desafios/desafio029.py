"""
Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite.
"""
quilômetros_por_hora = int(input('Digite a velocidade do carro: '))
if quilômetros_por_hora <=80:
    print(f'Seu carro está a {quilômetros_por_hora}Km. Pode seguir.')
else:
    print(f'Você foi multado! Seu carro está a {quilômetros_por_hora}Km, por isto, sua multa é de R${(quilômetros_por_hora - 80) * 7.00:.2f}.')
