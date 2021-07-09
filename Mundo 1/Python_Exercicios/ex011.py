altura = float(input('Digite a altura da parede: '))
largura = float(input('Digite a largura da parede: '))

area = altura * largura

print('Será necessário {:.2f} litros de tinta para pintar a parede'.format(area / 2))
