class Serie:
    #"episodios"
    def __init__(self, nombre, genero, popularidad, ):
        self.nombre = nombre
        self.genero = genero
        self.popularidad = popularidad
        #self.episodios = episodios
        #Implementacion para Arbol General
        self.hijos = []
        self.siguiente_serie = None