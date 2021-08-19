
Numero_inicial = int(input('Digite el comienzo de la lista: '))
Numero_final = int(input('Digite el final de la lista: '))
Intervalo = int(input('Digite el intervalo de repeticion: '))
total=0 
for i in range(Numero_inicial,Numero_final,Intervalo):
  total+= i 
  print(i)
print('La suma es:',total)