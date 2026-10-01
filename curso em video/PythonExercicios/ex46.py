from time import sleep

fogos = int(input("Quantos fogos de artificios estouraram?"))

for c in range(10, -1, -1):
    sleep(0.5)
    print(c)
    if c == 0:
        for c in range(1,fogos+1):
            sleep(0.3)
            print("POOOW!")
print(f"Foram {fogos} fogos.")