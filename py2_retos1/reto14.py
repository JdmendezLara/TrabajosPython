a =-10
def calculos(a):
  numeros_cuadrados = []
  while (a < 11):
    numeros_cuadrados.append(a**2)
    a+=1
  return(numeros_cuadrados)
def finalizado():
  print("programa finalizado")
print(calculos(a))
finalizado()
