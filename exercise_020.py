# A program that reads an inputed number and returns its ones, tens, hundreds, and thousands digits.

numero = int(input("Digite um numero de 0 a 9999: "))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
print('Unidade:', u)
print('Dezena:',  d)
print('Centena:', c)
print('Milhar:', m)
