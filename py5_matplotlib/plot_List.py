listadenumeros = []
valor = int(input("Digite el numero que sera evaluado: "))

while valor != 1:
  listadenumeros.append(valor)
  if (valor%2) == 0:
    valor = valor // 2
  else:
    valor = valor*3 + 1
    
listadenumeros.append(valor)    

print(listadenumeros)

