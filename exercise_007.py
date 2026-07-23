# to know the multiplication table of a number

print('Para descobrir a tabuada de um número')
nc1 = int(input('Digite o número:'))
print(nc1*0, nc1*1, nc1*2, nc1*3, nc1*4, nc1*5, nc1*6, nc1*7, nc1*8, nc1*9, nc1*10)

# the newest version use for to show the multiplication in a better format

print('Para saber a tabuada de 1x a 10x...')
d1 = int(input('Escreva o número que quer saber a tabuada: '))
for d2 in range(1, 11):
    print('| {} x {} | = {} '.format(d1, d2, d1*d2))
