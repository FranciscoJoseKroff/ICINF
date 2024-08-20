class Personaje:
    def __init__(self, vida, nombre, df):
        self.vida = vida
        self.nombre = nombre
        self.df = df
    
    def mostrar_info(self):
        print(f"El personaje {self.nombre} tiene {self.vida} de vida y {self.df} de daño físico.")
    
    def atacar(self):
        print(f"El personaje {self.nombre} ataca con {self.df} de daño físico.")

    def defenderse(self):
        print(f"El personaje {self.nombre} se defendió.")

    def esquivar(self):
        print(f"El personaje {self.nombre} esquivó el ataque.")
        
    def morir(self):
        print(f"El personaje {self.nombre} ha muerto.")

class Libro:
    def __init__(self, capitulos, titulo, autor):
        self.capitulos = capitulos
        self.autor = autor
        self.titulo = titulo

    def mostrar_info(self):
        if self.capitulos < 10:
            print(f"El título del libro es {self.titulo}, del autor {self.autor}, y tiene {self.capitulos} capítulo.")
        else:
            print(f"El título del libro es {self.titulo}, del autor {self.autor}, y tiene {self.capitulos} capítulos.")

    def abrir(self, capitulo):
        print(f"Se abrió el libro {self.titulo} en el capítulo {capitulo}.")
    
    def cerrar(self):
        print(f"Se cerró el libro {self.titulo}.")
    
    def quemar(self):
        print(f"El libro {self.titulo} se ha quemado.")

    def leer(self):
        print(f"Se está leyendo el libro {self.titulo}.")

class Persona:
    def __init__(self, nombre, edad, pais):
        self.nombre = nombre
        self.edad = edad
        self.pais = pais
    
    def presentarse(self):
        if self.edad > 1:
            print(f"Hola, soy {self.nombre}, tengo {self.edad} años y soy de {self.pais}.")
        else:
            print(f"Hola, soy {self.nombre}, tengo {self.edad} año y soy de {self.pais}.")
    
    def hablar(self, mensaje):
        print(f"{self.nombre} está diciendo: {mensaje}")

    def sentarse(self):
        print(f"{self.nombre} se ha sentado.")

    def mudarse(self, pais_nuevo):
        print(f"{self.nombre} se ha mudado al país {pais_nuevo}.")

    def muerte(self):
        print(f"{self.nombre} ha muerto.")

class Pc:
    def __init__(self, marca, procesador, ram):
        self.marca = marca
        self.procesador = procesador
        self.ram = ram

    def encender(self):
        print(f"El PC {self.marca} se está encendiendo.")

    def apagar(self):
        print(f"El PC {self.marca} se está apagando.")
 
    def reiniciar(self):
        print(f"La computadora {self.marca} se está reiniciando.")

    def abrir_programa(self, programa):
        print(f"Abriendo {programa} en el PC {self.marca}.")

    def mostrar_especificaciones(self):
        print(f"Las especificaciones son -> Marca: {self.marca}, Procesador: {self.procesador}, RAM: {self.ram} GB.")

class Restaurante:
    def __init__(self, nombre, capacidad, ubicacion):
        self.nombre = nombre
        self.capacidad = capacidad
        self.ubicacion = ubicacion

    def abrir(self):
        print(f"El restaurante {self.nombre} ha abierto.")

    def cerrar(self):
        print(f"El restaurante {self.nombre} ha cerrado.")

    def reservar(self, personas):
        if personas <= self.capacidad:
            if personas < 2: 
                print(f"La reserva de {personas} persona ha sido realizada con éxito.")
            else:
                print(f"La reserva de {personas} personas ha sido realizada con éxito.")
        else:
            print(f"La reserva de {personas} personas sobrepasa la capacidad máxima: {self.capacidad}.")
           
    def cambiar_menu(self, nuevo_menu):
        print(f"El restaurante {self.nombre} ha cambiado el menú a {nuevo_menu}.")

    def mostrar_info(self):
        print(f"Restaurante: {self.nombre}, Capacidad: {self.capacidad}, Dirección: {self.ubicacion}.")

pj1 = Personaje(568, "Heimerdinger", 56)
pj2 = Personaje(600, "Yasuo", 65)
pj3 = Personaje(608, "Mago", 54)

l1 = Libro(12, "Grand Blue", "Kenji Inoue")
l2 = Libro(8, "La lluvia sabe por qué", "María Fernanda Heredia")
l3 = Libro(15, "Boy's abyss", "Ryo Minenami")

per1 = Persona("Juan", 30, "España")
per2 = Persona("María", 25, "México")
per3 = Persona("Carlos", 40, "Argentina")

pc1 = Pc("Dell", "Intel i7", "16")
pc2 = Pc("HP", "AMD Ryzen 5", "8")
pc3 = Pc("Mac", "M1", "8")

r1 = Restaurante("Los sabores de Juanita", 50, "Yumbel 897")
r2 = Restaurante("Café Blanco", 100, "Blanco Encalada 268")
r3 = Restaurante("Sanguche patito", 30, "Gamboa 495")
