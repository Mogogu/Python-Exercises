# the first method form converting value of an input number of meters into his value on lower and higher forms of mesure
# we do the variables of each form of mesure (based on meters) and in the end we print them

print('Para saber quantos metros são em conversão de outras medidas.')
nb1 = float(input('Digite o valor em metros: '))
nbkm = nb1/1000
nbhm = nb1/100
nbdam = nb1/10
nbdm = nb1*10
nbcm = nb1*100
nbmm = nb1*1000
print('Os valores obtidos são: {}km, {}hm, {}dam, {}m, {}dm, {}cm, {}mm'.format(nbkm, nbhm, nbdam, nb1, nbdm, nbcm, nbmm))
