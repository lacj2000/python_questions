numbers = ['0','1','2','3','4','5','6','7','8','9']
def get_float (string):
    number = ''
    has_dot = False 
    after_dot = 0
    for letter in string:
        if has_dot and after_dot >= 2:
            break
        if letter == '.' and not has_dot:
            number += letter
            has_dot = True

        if letter in numbers:
            number += letter
            if has_dot:
                after_dot += 1
        
    return float(number)

st1 = input()
st2 = input()

cpf = ''
cont = 0
while len(cpf) < 11:
    if st1[cont] in numbers:
        cpf+=st1[cont]
    cont += 1

sum =  get_float(st1[cont:]) + get_float(st2)

print(f'cpf {cpf}')
print(f'{sum:.2f}')

