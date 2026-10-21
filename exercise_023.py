# A code that reads a sentence and show how many letters "Aa" it has

frase = str(input('Digite uma frase: ')).strip()
transforme = frase.lower()
quantidade = transforme.count('a')
primeira = transforme.find('a')
ultima = transforme.rfind('a')
print('Tem {} letras "a" na sua frase. A primeira na posição {}, e a última na posição {}.'. format(quantidade, primeira, ultima))
