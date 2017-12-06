# Faça um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar.

real = float(input('Quantos vc tem em dinheiro na moeda real ? R$: '))
dolar = real / 3.32

print('Com R$ {:.2f} você pode comprar USS {:.2f}'.format(real,dolar))