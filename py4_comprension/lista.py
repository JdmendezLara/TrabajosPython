B = [5,6,7,9]
A = [1,2,3,4]

C = []
n = len(A)//2
lista = [(((A[i+1])^2)*B[2*i])+B[n+i] for i in range(n)]
C.append(lista)
print("La lista es: ")
print(C)
