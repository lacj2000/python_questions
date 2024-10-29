frase = input('digite uma frase: ')

a = frase.lower().count('a')
a_p = frase.lower().find('a') + 1
a_p_l = len(frase) - frase[::-1].lower().find('a') 

print("""
Numero de ocorrencias 'a': {}
Primeira aparição 'a': {}ª
Última aparição 'a': {}ª
""".format(a, a_p, a_p_l))