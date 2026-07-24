# A program that shows how much you spent on a rental car based on how many days you kept it.

ni1 = int(input('Para saber quanto você gastou com o aluguel, digite o número de dias que manteve o veículo:'))
ni2 = int(input('Agora digite quantos quilometros você dirigiu:'))
ni3 = ni1*60
ni4 = ni2*0.15
ni5 = ni4+ni3
print('Pelo tempo de {}, irá pagar R${:.2f}. Pela distância de {}Km, irá pagar R${:.2f}. O total é R${:.2f}'.format(ni1, ni3, ni2, ni4, ni5))
