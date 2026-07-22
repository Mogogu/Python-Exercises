#This exercise is to convert one value in meters, input from the user, to different measures of the same category

print('Para saber quantos metros são em conversão de outras medidas.')
nb1 = float(input('Digite o valor em metros:'))
nbkm = nb1/1000
nbhm = nb1/100
nbdam = nb1/10
nbdm = nb1*10
nbcm = nb1*100
nbmm = nb1*1000
print('Os valores obtidos são: {}km, {}hm, {}dam, {}m, {}dm, {}cm, {}mm'.format(nbkm, nbhm, nbdam, nb1, nbdm, nbcm, nbmm))
