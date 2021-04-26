def Llenado_de_lista(A,B):
  n = len(A)//2
  C = []
  for i in range(n):
    d = ((A[i+1])**2)
    e = d * (B[2*i])
    f = e + B[n + i]
    C.append(f)
  print("La lista es: ")
  print(C)
  return C

B = [5,6,7,9]
A = [1,2,3,4]
Llenado_de_lista(A,B)
    
