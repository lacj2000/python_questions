nome = input('digite seu nome: ')

primeiro = nome.split()[0]
#ultimo = nome[::-1].split()[0][::-1]
ultimo = nome.split()[len(nome.split())-1]

print('Primeiro nome: {}\nÚltimo nome: {}'.format(primeiro, ultimo))