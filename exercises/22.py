name =  input("Nome: ")
upper = name.upper()
lower = name.lower()
size = len(name)- name.count(' ') 
first_name = len(name.split()[0])

print("""
Maiusculo: {}
minusculo: {}
tamanho sem espacos: {}
tamanho do primeiro nome: {}
""".format(upper, lower, size, first_name))