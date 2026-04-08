sal = float(input('Qual o valor do salario do funcionario? '))

new_salario = sal + (sal * 15 / 100)

print('O funcionario que ganhava R${:.2f}, vai passar a ganhar R${:.2f}, apos o aumento.'.format(sal, new_salario))