print("Gerador de PA")
print("-=-" * 10)

primeiro = int(input('Primeiro termo: '))
razao = int(input("Razao da PA: "))
termo = primeiro
cont = 1
total = 0
mais = 10

while mais != 0:
    total += mais
    while cont <= total:
        print(f'{termo} -> ', end='')
        termo += razao
        cont += 1

    print("Pausa!")
    mais = int(input("QUanros termos vc quer mostrar a mais? "))
print("Progressao finalizada com {} termos!".format(total))
