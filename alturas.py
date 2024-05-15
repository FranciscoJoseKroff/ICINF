suma_alturas = 0
cont = 0

while True:
    altura = float(input("Ingrese la altura en metros (0 para finalizar): "))
    if altura == 0:
        break
    suma_alturas += altura
    cont += 1

if cont > 0:
    altura_promedio = suma_alturas / cont
    print("La altura promedio de las personas es:", altura_promedio, "metros")
else:
    print("No se ingresaron alturas.")

