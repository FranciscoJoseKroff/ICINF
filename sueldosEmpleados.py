empleados_500_900 = 0
empleados_mas_900 = 0
total_gastos = 0

while True:
    sueldo = int(input("Ingrese el sueldo mensual del empleado (-1 para finalizar): "))
    if sueldo == -1:
        break
    total_gastos += sueldo
    if 500000 <= sueldo <= 900000:
        empleados_500_900 += 1
    elif sueldo > 900000:
        empleados_mas_900 += 1

print("Empleados que cobran entre $500.000 y $900.000:", empleados_500_900)
print("Empleados que cobran más de $900.000:", empleados_mas_900)
print("La empresa gasta en total: $", total_gastos)
