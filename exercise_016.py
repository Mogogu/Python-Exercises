# using from math, squareroot and power, we can calculate the hypotenuse
# we create two variables to receive both legs, power them by two
# the result come from using sqrt in the sum of both powered legs

from math import sqrt, pow
hipotenusa é a raíz quadrada da soma dos quadrados dos catetos. ex.: ca*ca + co*co = h*h
ca = float(input('Informe o cateto adjacente:'))
co = float(input('Informe o cateto oposto:'))
hipotenusa = sqrt(pow(ca,2)+pow(co,2))
print('A hipotenusa é:{}'.format(hipotenusa))
