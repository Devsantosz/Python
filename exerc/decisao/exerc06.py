n1 = int(input('Digite um numero: '))
n2 = int(input('Digite um numero: '))
n3 = int(input('Digite um numero: '))

if n1 > n2 and n1 > n3:
    print(f"O maior numero é {n1}")
elif n2 > n1 and n2 > n3:
    print(f"O maior numero é {n2}")
else:
    print(f"O maior numero é {n3}")