lista=[]
factor_conversion=950
for x in range(10):
    dolar=int(input("Ingrese 10 precios de productos en dólares: "))
    lista.append(dolar)
listaPesos=[]
for x in lista:
    precio_clp=factor_conversion*x
    print("La conversión del producto" ,x, "a CLP es: ", precio_clp)
