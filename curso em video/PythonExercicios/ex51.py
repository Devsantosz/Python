#Progressao Aritmeticas

pri_termo = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razao: "))
dec = pri_termo + (10 - 1) * razao
for c in range(pri_termo, dec + razao, razao):
   print(f"{c} x ", end="")
print("FIM")