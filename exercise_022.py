# A program that reads if a inputed name has "silva" in it

nomede = str(input('Digite seu nome: ')).strip()
if nomede.find('silva') == -1:
    print ('Seu nome não possui Silva')
else:
    print ('Seu nome possui Silva')
