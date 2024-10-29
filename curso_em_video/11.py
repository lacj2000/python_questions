height = float(input('Digite o a altura da parede em metros: '))
width = float(input('Digite o a largura da parede em metros:'))

print('Para pintar {:.2f}m² em paredes, com uma tinta com rendimento de 2m² por litro:\nsão(é) nescessário(s) {:.2f} litros de tinta'.format(width*height,width*height/2))