#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a asua area e a quantidade de tinta necessaria para pinta-la.
#Sabendo que cada litro de tinta, pinta uma area de 2m quadrado.

largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))

area = largura * altura

print('Sua parede tem a dimensão de {} x {} e sua área é de {} m².'.format(largura,altura,area))

tinta = area/2

print('Para pintar essa parede, você precisara de {} litros de tinta.'.format(tinta))





