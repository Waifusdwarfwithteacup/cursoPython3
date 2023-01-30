"""
O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
Faça um programa que leia o nome dos quatros alunos e mostre a ordem sorteada.
"""
from random import shuffle
nome_dos_alunos = []
for contador in range(1,5):
    nome_do_aluno = input(f'Digite o nome do(a) {contador}º(a) aluno(a): ')
    nome_dos_alunos.append(nome_do_aluno)
shuffle(nome_dos_alunos)
print(f' A ordem de apresentação, será essa: {nome_dos_alunos}.')
