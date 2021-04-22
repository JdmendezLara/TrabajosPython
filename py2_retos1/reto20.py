def añobisiesto(a):
  if a%4==0 and (not(a%100==0) or a%400==0 ):
    texto='es bisiesto.'
  else:
    texto='es un año NO bisiesto.'
  return texto
a=int(input('Introduzca un año entre 1600 y 2500:'))
print(a,añobisiesto(a))
