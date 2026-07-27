# function choice(), sample() and shuffle()
# We list four students and print the choice from the system.
# Creating a list with [] groups the names together.

import random

aluno1 = input('Digite o nome do aluno: ')
aluno2 = input('Digite o nome do aluno: ')
aluno3 = input('Digite o nome do aluno: ')
aluno4 = input('Digite o nome do aluno: ')
alunos = [aluno1, aluno2, aluno3, aluno4]
sorteio = random.choice(alunos)
#random.shuffle(alunos)
sorteio1 = random.sample(alunos, 4)
print ('O aluno escolhido pelo sistema foi {}'.format(sorteio))
print ('A sequência de alunos escolhidos pelo sistemas foi: {}'.format(sorteio1))
