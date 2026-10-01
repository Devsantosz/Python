from time import sleep

fogos = int(input("Quantos fogos de artificios estouraram?"))

for c in range(1,fogos+1):
    sleep(0.5)
    print(f"POOOW - {c} estouro!")
print(f"Foram {fogos} fogos.")