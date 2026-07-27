# using functions from math (sin, cos, tan, radians)
# the program ask the degrees and return the value in radians, them use radians to calculate sin, cos and tan 

from math import sin, cos, tan, radians
angulo = float(input('Digite um angulo: '))
radianos = radians(angulo)
sen0 = sin(radianos)
cos0 = cos(radianos)
tan0 = tan(radianos)
print('Para o ângulo {}, o resultado é: seno {:.2f}, cosseno {:.2f}, tangente {:.2f}'.format(angulo, sen0, cos0, tan0))
