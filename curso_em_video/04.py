value = input('Typing something: ')

print('Text type: {}'.format(type(value)))
print('This text has only space: {}'.format(value.isspace()))
print('This text has only alpha: {}'.format(value.isalpha()))
print('This text has only numeric: {}'.format(value.isnumeric()))
print('This text is alphanumeric: {}'.format(value.isalnum()))
print('This text has only uppercase: {}'.format(value.isupper()))
print('This text has only lowercase: {}'.format(value.islower()))
print('This text has capitalize: {}'.format(value.istitle()))