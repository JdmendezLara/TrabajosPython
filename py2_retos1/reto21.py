def IMC(masa,altura):
  imc = masa/(altura**2)
  return(imc)

m = float(input("Especifique su masa coorporal: "))
print("Masa = ",m,"Kg")

a = float(input("Especifique su altura: "))
print('Altura =',a,'m')  

print('Tu Indice de Masa Corporal es',round(IMC(a,m),2))  
