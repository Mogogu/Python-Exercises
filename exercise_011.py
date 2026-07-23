# an exercise that shows the increase of 15% in the monthly payment

print('Para descobrir um aumento no seu salário')
ng1 = float(input('Digite o valor de seu salário mensal:'))
ng2 = (ng1/100)*15
ng3 = ng1 + ng2
print('O aumento de 15% no seu salário, equivale à {:.2f}, e o novo total é {:.2f}'.format(ng2, ng3))
