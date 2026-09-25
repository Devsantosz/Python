distancia = float(input("Digite a distancia da viagem: "))
print(f"Voce esta preste a comecar uma viagem de {distancia}Km.")

#valor_via = distancia * 0.50 if distancia <= 200 else distancia * 0.45
#Condicao simplificada das condicoes abaixo

if distancia <= 200:
    valor_via = distancia * 0.50
    
else:
    valor_via = distancia * 0.45
print(f"O valor da viagem foi de R${valor_via} por {distancia}Km.")


