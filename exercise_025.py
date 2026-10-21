# A code where the computer chose a number in between 0 and 5, then ask for the user try to find out the number the machine chose;
# If the number was the same, the user wins and show "Parabéns! Você venceu.", if not, "A máquina venceu!"

import random
dado = [0, 1, 2, 3, 4, 5]
escolha = random.choice(dado)
escolhauser = int(input('Escolha um número entre 0 e 5 para competir:'))
if escolhauser == escolha:
    print('Parabéns! Você venceu.')
else:
    print('A máquina venceu!')
print('A máquina escolheu {}'.format(escolha))
