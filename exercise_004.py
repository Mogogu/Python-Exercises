# to know the double, triple and squareroot of a number
# the first option is to print the results alone

print('Para saber o dobro, o triplo e a raiz quadrada de um número.')
n = int(input('Digite um número: '))
print(n*2, n*3, n**(1/2))

# we can improve the code to add precision
# usings new variables

print('Para saber o dobro, o triplo e a raiz quadrada de um número.')
na1 = int(input('Digite um número: '))
nab1 = na1 * 2
nab2 = na1 * 3
nab3 = na1 ** (1/2)
print('O dobro de {} é {}, o triplo é {}, e a raíz quadrada é {:.1f}'.format(na1, nab1, nab2, nab3))

# there are more options for the same code
# ones that can be more useful with "direct operation"

print('Para saber o dobro, o triplo e a raiz quadrada de um número.')
from math import sqrt
nb1 = int(input('Digite um número: '))
nbb1 = nb1 * 2
nbb2 = nb1 * 3
nbb3 = sqrt(nb1)
print('O dobro de {} é {}, o triplo é {}, e a raíz quadrada é {:.1f}'.format(nb1, nbb1, nbb2, nbb3))
