"""
Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
"""
from random import choice
nome_dos_alunos = []
for contador in range(1,5):
    nome_do_aluno = input(f'Digite o nome do(a) {contador}° aluno(a): ')
    nome_dos_alunos.append(nome_do_aluno)
print(f'O(a) aluno(a) sorteado(a) foi o(a): {choice(nome_dos_alunos)}.')