from random import choice

nome = str(input('INFORME O NOME DO PRIMEIRO JOGADOR POR FAVOR :'))
nome2= str(input('INFORME O NOME DO SEGUNDO JOGADOR POR FAVOR: '))

bvb=('BVB')
juve=('JUVE')
real=('REAL MADRID')
barca=('BARCELONA')
milan=('MILAN')
psg=('PSG')
bayer=( 'BAYER')
atl=('ATLETICO DE MADRID')
chelsea=('CHELSEA')

time = [bvb, juve,real,barca,milan,psg,bayer,atl,chelsea]
listatime = choice(time)
listatime2 =choice(time)

print('O Jogador {} vai jogar com {}'.format(nome,listatime))
print('O Jogador {} vai jogar com {}'.format(nome2,listatime2))