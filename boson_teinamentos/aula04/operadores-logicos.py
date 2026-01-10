#AND

idade = 25
altura = 1.75

resultado = (idade >= 18) and (altura >= 1.70)

msg = 'Pode participar do evento?' + str(resultado)
print(msg)

#OR
#Programa de disparo de alarme

porta = 'a'
janela = 'a'

alarme = (porta == 'a') or (janela == 'a')

msg = 'Alarme disparado? ' + str(alarme)
print(msg)

#NOT
tem_dinheiro = False
tem_dinheiro = not tem_dinheiro
msg = 'Tem dinheiro?' +  str( not tem_dinheiro)
print(msg)