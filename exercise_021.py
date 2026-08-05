# The program reads and answer if a city name start with "santo"

cidade = input('Digite o nome da cidade: ')
if cidade.find('Santo') == 0:
    print('Sua cidade começa com Santo')
else:
    print('Sua cidade não começa com Santo')
cidaded = cidade.strip().lower()
print('santo' in cidaded[0:6])
