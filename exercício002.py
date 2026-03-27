#Second exercise. To learn about the input
n = input('Digite algo: ')
print (type(n))
print('É número?', (n).isnumeric())
print('É letra?', (n).isalpha())
print('É alfanúmerico?', (n).isalnum())
print('Está em maiúsculo?', (n).isupper())
print('Está em minúsculo?', (n).islower())
print('É espaço?', (n).isspace())
