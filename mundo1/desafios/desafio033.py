"""
Faça um programa que leia três números e mostre qual é o maior número e qual é o menor.
"""
maior_número = 0
menor_número = 0
for i in range(1,4):
    número_digitado = int(input(f'Digite o {i}° número: '))
    if i == 1:
        maior_número = número_digitado
        menor_número = número_digitado
    elif i > 1:
        if maior_número < número_digitado:
            maior_número = número_digitado
        elif menor_número > número_digitado:
            menor_número = número_digitado
print(f'O maior número foi: {maior_número} e o menor número foi {menor_número}.')