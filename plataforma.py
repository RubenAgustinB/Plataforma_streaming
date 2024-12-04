from arbol_binario import Arbol_binario
from contenido import *
from usuario import *
from peliculas import *
from arbol_general_series import Arbol_General_Series
from cola_prioridades import ColaPrioridades

class Plataforma:
    def __init__(self, nombre):
        self.nombre = nombre

        self.arbol_usuarios = Arbol_binario()
        self.arbol_peliculas = Arbol_binario()
        self.catalogo = Catalogo()
        #self.arbol_series = Arbol_General_Series()
        self.watchlist = ColaPrioridades()

    #MANEJO DE USUARIOS

    def inicio_sesion(self):
        while True:
            print("\n1. Crear Usuario\n2. Iniciar Sesión\n3. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.crear_usuario()
            elif opcion == "2":
                usuario = input("Usuario: ")
                contrasena = input("Contraseña: ")
                if self.arbol_usuarios.buscar_usuario(usuario, contrasena):
                    self.menu_principal()
                else:
                    print("Usuario o contraseña incorrectos.")
            elif opcion == "3":
                print("¡Gracias por usar la plataforma!")
                break
            else:
                print("Opción no válida.")

    def crear_usuario(self):

        nombre = input("Nombre: ")
        contrasena = input("Contraseña: ")
        edad = int(input("Edad: "))
        # Se crea una instancia de la clase Usuario con los datos ingresados. 

        usuario= Usuario(nombre, contrasena, edad)
        self.arbol_usuarios.agregar_nodocontenido(usuario)
        #print(f"Usuario {nombre} creado con éxito.")
    
    #SECTOR PELICULAS

    def agregar_pelicula(self):
        # cambio kevin
        #Agrega una película al catálogo.
        
        print("\n--- Agregar Película ---")

        nombre = input("Nombre de la película: ").strip()
        genero = input("Género: ").strip()
        try:
            popularidad = int(input("Popularidad (número de visualizaciones): ").strip())
            duracion = int(input("Duración (en minutos): ").strip())
        except ValueError:
            print("Por favor, ingrese valores numéricos para popularidad y duración.")
            return

        pelicula= Pelicula(nombre, genero, popularidad, duracion)

        self.arbol_peliculas.agregar_nodocontenido(pelicula)
        
        
    def buscar_pelicula(self):

        #cambio kevin
        #Permite buscar una película por nombre.
        
        print("\n--- Buscar Película ---")
        nombre = input("Nombre de la película: ").strip()

        pelicula = self.arbol_peliculas.buscar_pelis(nombre)  
        if pelicula:
            print(f"Pelicula encontrada: {pelicula.nombre}, Género: {pelicula.genero}, Popularidad: {pelicula.popularidad}, Duración: {pelicula.duracion} minutos.")
        else:
            print(f"No se encontró la película '{nombre}'.")
    
    #SECTOR SERIES - Arreglar 

    def agregar_serie(self):
        print("\n--- Agregar Serie ---")
        nombre = input("Nombre de la serie: ")
        genero = input("Género: ")
        popularidad = int(input("Popularidad (número de visualizaciones): "))
        
        print("\n--- Agregar Capitulos a la Serie ---")

        # crear nodo hijo capitulo para serie
        #self.contenido.
        

       # print(f"La Serie '{nombre}' y sus '{cont_cap}' capitulo/s fueron agregados con éxito al catálogo.")
        
    def buscar_serie(self):
        print("\n--- Buscar Seire ---")

        nombre = input("Nombre de la Serie: ")

        self.series.mostrar_serie(nombre)

    #MENU PRINCIPAL

    def menu_principal(self):
        while True:
            print("\n--- Menú Principal ---")
            print("1. Ver contenido")
            print("2. Agregar película")  # Nueva opción
            print("3. Buscar Pelicula")
            print("4. Agregar Serie")
            print("5. Buscar Serie")
            print("6. Mas populares")
            print("7. Mostrar peliculas")
            print("8. Agregar a Watchlist")
            print("9. Mostrar Watchlist")
            print("10. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                #hay que trabajar en este juntando los dos arboles (serie y peli) en contenido
                self.catalogo.mostrar_contenido(self.arbol_peliculas)

            elif opcion == "2":  # Nueva funcionalidad agregar película

                self.agregar_pelicula()

            elif opcion == "3":

                self.buscar_pelicula()

            elif opcion == "4":  # Nueva funcionalidad agregar serie

                self.agregar_serie()

            elif opcion == "5": # Nueva funcionalidad buscar serie

                self.buscar_serie()
            
            elif opcion == "6":

                self.arbol_peliculas.peliculas_mas_populares()
            #tira error sin peliculas para hacer---vvvvvv
            elif opcion == "7":

                self.contenido.mostrar_peliculas()
            
            elif opcion == "8":
                self.agregar_a_watchlist()

            elif opcion == "9":

                self.mostrar_watchlist()

            elif opcion == "10":
                
                break

            else:
                print("Opción no válida.")

    # metodos de cola de prioridades
    def agregar_a_watchlist(self):
        
        #Permite al usuario agregar contenido a la watchlist.
        
        print("\n--- Agregar a Watchlist ---")
        nombre = input("Nombre del contenido: ").strip()
        try:
            prioridad = int(input("Prioridad (mayor número, mayor prioridad): ").strip())
        except ValueError:
            print("Por favor, ingrese un número válido para la prioridad.")
            return

        if self.contenido.peliculas.buscar_pelicula(nombre):
            self.watchlist.agregar_contenido(nombre, prioridad)
            print(f"'{nombre}' fue agregado a la watchlist con prioridad {prioridad}.")
        else:
            print(f"El contenido '{nombre}' no está disponible en el catálogo.")

    def mostrar_watchlist(self):
        
        #Muestra los contenidos en la watchlist.
        
        print("\n--- Watchlist ---")
        self.watchlist.mostrar_contenido()






