# A program that show the name of a person in uppercase and lowercase, then show how many letters there are and the spaces

nome = str(input('Digite seu nome: '))
print('Seu nome em maiúsculo é: ', nome.upper())
print('Seu nome em minúsculo é: ', nome.lower())
nomes = nome.split()
nomel = len(''.join(nomes))
print('Seu nome tem {} letras'.format(nomel))
print('Sem espaços seu primeiro nome tem {} letras'.format(len(nomes[0])))
