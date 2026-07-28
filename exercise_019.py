# A program that turn you name (string input), into uppercase, then lowercase
# then we use function "len" to know how many letters there are
# in the end we use len again to know how many spaces there are

nome = str(input('Digite seu nome: '))
print('Seu nome em maiúsculo é: ', nome.upper())
print('Seu nome em minúsculo é: ', nome.lower())
nomes = nome.split()
nomel = len(''.join(nomes))
print('Seu nome tem {} letras'.format(nomel))
print('Sem espaços seu primeiro nome tem {} letras'.format(len(nomes[0])))
