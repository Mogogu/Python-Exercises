# a code created to show the user how many liters of paint he need to cover a wall
# the user defines how tall and large is the wall and the program return the liters of paint

print('Para saber a área total de uma parede, e o quanto de tinta precisa para pintar, responda:')
ne1 = float(input('Quantos metros tem a largura da parede?'))
ne2 = float(input('Quantos metros tem a altura da parede?'))
ne3 = 2**2
print('Sua parede tem', ne1*ne2, 'e precisará de:', (ne1*ne2)/ne3, 'litros de tinta.')
