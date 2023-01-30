"""
Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados.
Ex:
Digite um número: 1834.
unidade: 4.
dezena:3.
centena:8.
milhar:1.
"""
número_digitado = int(input('Digite um número '))
número_convertido_em_texto = str(número_digitado)
digitos_separados = []
contador = len(número_convertido_em_texto)
if número_digitado>=0 and número_digitado<=9999:
    for i in range(0, contador):
        digitos_separados.append(número_convertido_em_texto[i])
else:
    print(f'O valor {número_digitado} não é válido!')
digitos_separados = digitos_separados[::-1]
if contador == 4:
    print(f'Unidade: [{digitos_separados[0]}], Dezena: [{digitos_separados[1]}], Centena: [{digitos_separados[2]}], Milhar: [{digitos_separados[3]}].')
elif contador == 3:
    print(f'Unidade: [{digitos_separados[0]}], Dezena: [{digitos_separados[1]}], Centena: [{digitos_separados[2]}].')
elif contador == 2:
    print(f'Unidade: [{digitos_separados[0]}], Dezena: [{digitos_separados[1]}].')
else:
    print(f'Unidade: [{digitos_separados[0]}].')