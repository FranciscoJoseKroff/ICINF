def potencia(num,exp):
     if exp==0:
          return 1
     elif exp==1:
          return num
     else:
          return num*potencia(num,exp-1)

print(potencia(2,3))
