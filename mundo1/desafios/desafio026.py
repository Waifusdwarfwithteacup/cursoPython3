"""
Faça um programa que leia uma frase pelo teclado e mostre:
- Quantas vezes aparece a letra "A".
- Em que posição ela aparece a primeira vez.
- Em que posição ela aparece na última vez.
"""
frase = input('Digite uma frase: ').upper()
if frase.find("A") == -1:
    print('A palavra A aparece [0] vezes, Ela aparece pela primeira vez na posição: [Nenhuma] e na última vez que ela aparece é na posição: [Nenhuma].')
else:
    print(f'A palavra A aparece [{frase.count("A")}] vezes, Ela aparece pela primeira vez na posição: [{frase.find("A")}] e na últina vez que ela aparece é na posição: [{frase.rfind("A")}].')
