largura = float(input('Qual a largura da parede? '))
altura = float(input('Qual a altura da parede? '))
area = largura * altura

tinta = area / 2

print('Sua parede tem {}x{} e sua area e de {}m2.'.format(largura, altura, area))
print('Para pintar essa parede, vice precisara de {}L de tinta.'.format(tinta))