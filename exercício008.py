# this code is for the conversion of the exchange of brazilian currency for the USA currency
# simple code of a float input for the BRL and the result in DOL
# then we print, showing the results

print('Para descobrir quantos dólares você compra com um valor em real, na cotação de 5,00 o dólar')
brl = float(input('Digite o valor em real: '))
dol = brl / 5
print('A quantidade que você disse, em real, foi {:.2f}BRL e a conversão resultou em {:.2f}DOL.'.format(brl, dol))
