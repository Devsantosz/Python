# Programa para calcular excesso de peso de peixe e multa correspondente
kg_peixe = float(input("Digite a quantidade de quilos de peixe: "))

if kg_peixe <= 50:
    excesso = 0
    multa = 0
    print("Não houve excesso de peso. Não há multa.")
else:
    excesso = kg_peixe - 50
    multa = excesso * 4.00
    print(f"Houve excesso de peso de {excesso:.2f} kg.")
    print(f"A multa a ser paga é de R$ {multa:.2f}.")