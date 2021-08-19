import random
x = random.randrange(300)
print('El valor es: ',x)

if x < 10:
  print ('El valor generado es menor que 10.')
if x >= 10:
  if x <= 50:
     print ('El valor generado esta en elintervalo de 10 a 50.')
if x > 50:
  if x <= 100:
     print ('El valor generado esta en elintervalo de 10 a 50.')
if x > 100: 
  print ('El valor generado es mayor que 100.')