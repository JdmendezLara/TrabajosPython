A = [4,5,6,7]
B = [5,6,7,9]
C = [1,2,3,4]

n = len(A)
acumulador = sum((A[i]*B[i])+C[i] for i in range(n))+ n^2
print("El resultado de la sumatoria es: ")
print(acumulador)