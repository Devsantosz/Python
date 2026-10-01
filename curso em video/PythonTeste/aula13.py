from time import sleep

num = 0
for c in range(0,15):
    num = num + 1
    sleep(1)
    print(f"Oi! {num}")
print("Fim")