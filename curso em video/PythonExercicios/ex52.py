num = int(input("Digite um numero primo: "))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print(f"\033[33m", end=" ")
        tot += 1
    else:
       print(f"\033[31m", end=" ") 
    print(f"{c}", end=" ")
print(f"\nO numero {num}, foi divisivel {tot} vezes.")
if tot == 2:
    print("E por isso ele e primo!")
else:
    print("Por isso ele nao e primo!")
    