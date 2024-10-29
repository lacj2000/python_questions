numero = input('Digite um numero de 0 a 999: ')

numero_ = int(numero)

unidade_ = numero_ % 10
dezena_ = numero_ // 10 % 10
centena_= numero_ // 100 % 10
milhar_ = numero_ // 1000 % 10



print("""Matematicamente
Unidade: {}      
Dezena: {}      
Centena: {}      
Milhar: {}      
      """.format(unidade_, dezena_, centena_, milhar_))


reverse = numero[::-1] 
unidade = reverse[0] if len(reverse) > 0 else 0  
dezena = reverse[1] if len(reverse) > 1 else 0 
centena = reverse[2]  if len(reverse) > 2 else 0 
milhar = reverse[3]  if len(reverse) > 3 else 0 

print("""Metodos de String
Unidade: {}      
Dezena: {}      
Centena: {}      
Milhar: {}      
      """.format(unidade, dezena, centena, milhar))
