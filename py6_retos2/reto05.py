import random
listadenumeros = []
a = int(input('Cantidad de numeros que desea ver:'))
i= 0
while i < a:
  i = i + 1
  x = random.randrange(101)
  listadenumeros.append(x)

print('Los numeros son: ',listadenumeros)