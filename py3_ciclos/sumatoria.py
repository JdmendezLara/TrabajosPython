def sumatoria(A,B,C):
  acumulador = 0
  n = len(A)
  for i in range(n):
    d = A[i]*B[i]
    e = d + C[i]
    f = e + n**2
    acumulador = acumulador + f
  print("El resultado es: ")
  print(acumulador)
  
  return acumulador
  
A = [4,5,6,7]
B = [5,6,7,9]
C = [1,2,3,4]
sumatoria(A,B,C)



