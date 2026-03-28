# for knowing the predecessor and successor of a number
# calculates the variable with plus and minus results

print('Para saber o antecessor e o sucessor de um número')
n = int(input('Digite um número: '))
print(n - 1, n, n + 1)

# the other form consists in using new variables and some changes in the command print

print('Para saber o antecessor e o sucessor de um número')
na1 = int(input('Digite um número: '))
nb1 = na1 + 1
nb2 = na1 - 1
print('O antecessor do número {} é {}, e o sucessor é {}'.format(na1, nb2, nb1))
