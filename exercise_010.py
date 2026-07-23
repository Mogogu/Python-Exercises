# an exercise that shows the value of an item after 5% discount

print('Para calcular um desconto de 5% sobre o valor de um item/objetivo:')
nf1 = float(input('Qual o preço do item?'))
nf2 = (nf1/100) * 5
nf3 = nf1-nf2
print('Com o desconto de 5%, seu item de {} sai à {:.2f}'.format(nf1, nf3))
