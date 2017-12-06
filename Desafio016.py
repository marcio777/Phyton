# crie um programa que leia um numero real e mostre sua porção inteira.
# exemplo digita um numero 6.127 tem a parte inteira 6.

import math

num = float(input('Digite um numero '))
num = math.floor(num)
print('O numero digitado foi {}'.format(num))
