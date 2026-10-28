from math import factorial
n = int(input("Digite um numero \nPara calcular a fatorial: "))
c = n
f = 1
print("Calculando a fatorial de {}!".format(n))
while c > 0 :
    print('{}'.format(c), end=' ')
    print(" x " if c > 1 else "= ", end='')
    f *= c
    c-=1
print(f"{f}")