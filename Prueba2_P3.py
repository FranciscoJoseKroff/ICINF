paises={}

for x in range (5):
    pais=input("Ingrese un pais: ")
    capital=input("Ingrese capital del país dado: ")
    paises[pais]=capital

turista=input("Ingrese nombre del turista: ")
paisTurista=input("Ingrese pais de procedencia: ")

print("El turista", turista, "viene del pais", paises[pais], "y su capital es:", capital)
