from series import Serie
class Arbol_General_Series:
    def __init__(self):
        self.sig = None
        self.hijos = None

#PARA TERMINAR VER IMPLEMENTACION DE CAPITULOS

    def agregar_hijo_raiz(raiz,serie):
        raiz.agregar_nodo(raiz,serie)

    def agregar_nodo(raiz,serie):
        nodo = Serie(serie)
        if (raiz.hijos is None):
            raiz.hijos = nodo
        else:
            anterior = raiz.hijos
            actual = raiz.hijos.siguiente_serie
            while (actual is not None):
                anterior=anterior.siguiente_serie
                actual = actual.siguiente_serie
            anterior.siguiente_serie = nodo
            nodo.siguiente_serie = actual

        return raiz

    #def agregar_hijo_nodo(raiz,nodo,info):
        #anterior = raiz.hijos
       # actual = raiz.hijos.siguiente
       # ok = False

       # while(actual is not None) and (not ok):
           # if anterior.info == nodo:
             #   ok = True
            #else:
             #   anterior = anterior.siguiente
            #    actual = actual.siguiente
       # if ok:
       #     nodo = raiz.agregar_nodo(anterior,info)
       # anterior.siguiente = nodo
       # nodo.sig = actual
    

            
   