k = 0
for l in range(64):
  k+= 2**l
  print(l+1,2**l,k)
print("En notación científica es %e,\n y el total es: %E granos de trigo." % (2**l,k))

