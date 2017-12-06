preco = float(input('Informe o valor do produto: '))
novo = preco -(preco * 10 / 100)
print('O produto que custava R${:.2f}, na promoção  de pagamento a vista  desconto de 10% vai custar R$ {:.2f}'.format(preco,novo))
novo2 = preco - (preco * 3 / 100)
print('O produto a prazo vai custar {:.2f}'.format(novo2))


