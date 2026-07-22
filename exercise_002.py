# second exercise. To learn about the input
# basically i'm using native commands to return 'false' or 'true' for characteristics of the input digit

print('Considere que "false" é "falso", e "true" é "verdadeiro"...')
n = input('Digite algo: ')
print (type(n))
print('É número?', (n).isnumeric())
print('É letra?', (n).isalpha())
print('É alfanúmerico?', (n).isalnum())
print('Está em maiúsculo?', (n).isupper())
print('Está em minúsculo?', (n).islower())
print('É espaço?', (n).isspace())
