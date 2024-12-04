from arbol_binario import *


class Catalogo:
    """
    Clase que gestiona el catálogo de películas y series de la plataforma.
    """
    def __init__(self):
        self
        
    def agregar_pelicula(self, nombre, genero, popularidad, duracion):
        """
        Agrega una película al árbol de películas.
        """
        self.peliculas.insertar_pelicula(nombre, genero, popularidad, duracion)
        #print(f"Película '{nombre}' agregada con éxito al catálogo.")

    def agregar_serie(self, nombre, genero, popularidad, episodios):
        """
        Agrega una serie a la lista de series.
        """
        self.series.append({"nombre": nombre, "genero": genero, "popularidad": popularidad, "episodios": episodios})
        print(f"Serie '{nombre}' agregada con éxito al catálogo.")

    def mostrar_contenido(self,arbol_peliculas:Arbol_binario):
        """
        Muestra el catálogo completo (películas y series).
        """
        print("\n--- Catálogo de Contenido ---")

        arbol_peliculas.mostrar_peliculas() #ok

        # Mostrar series: Es una lista, tenemos que modificarlo.
        # if self.series:
        #     print("\nSeries:")
        #     for serie in self.series:
        #         print(f"- {serie['nombre']} (Género: {serie['genero']}, Popularidad: {serie['popularidad']}, Episodios: {serie['episodios']})")
        # else:
        #     print("No hay series disponibles.")

   