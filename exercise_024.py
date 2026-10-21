# A code that ask for the user name, and show the first and last name

nomec = str(input('Digite seu nome: ')).strip()
nomecs = nomec.split()
print(nomecs[0], nomecs[-1])
