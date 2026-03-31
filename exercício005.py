# to know the stundent's average grade
# the average number in between two inputed numbers
# for the first model we use float, because it's better for grades in general

print('Para saber a média entre duas notas')
n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
print(n1, 'e', n2, 'sua média é:', (n1 + n2)/2)

# the second model is more efficient

print('Para saber a média entre duas notas de um aluno.')
nb1 = float(input('Digite a primeira nota: '))
nb2 = float(input('Digite a segunda nota: '))
result = (nb1 + nb2) / 2
print('A média entre {} e {} é {:.1f}.'.format(nb1, nb2, result))
