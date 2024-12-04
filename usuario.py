class Usuario:
    
    def __init__(self, nombre, contrasena, edad):
        self.nombre = nombre
        self.contrasena = contrasena
        self.edad = edad
        self.historial_visualizacion = []
        self.preferencias = []
        #Intanciamos para utilizar la clase como nodo
        self.izquierdo = None
        self.derecho = None

    def __str__(self):
        return self.nombre