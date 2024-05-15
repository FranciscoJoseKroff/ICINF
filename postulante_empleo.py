preguntas=int(input("Ingrese la cantidad de preguntas"))
correct=int(input("Ingrese cantidad de preguntas correctas"))

porcentaje= (correct/preguntas)*100
if porcentaje >= 95:
    nivel = "Nivel máximo"
elif porcentaje >= 70:
    nivel = "Nivel medio"
elif porcentaje >= 40:
    nivel = "Nivel regular"
else:
    nivel = "Fuera de nivel"

print("El nivel del postulante es:", nivel)