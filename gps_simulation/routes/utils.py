import heapq #libreria para implementar la cola de prioridad
from .models import City, Route


def dijkstra(ciudad_inicio):
    distancias = {ciudad_inicio: 0}
    ciudades_previas = {ciudad_inicio: None}
    cola_prioridad = [(0, ciudad_inicio)]

    while cola_prioridad:
        distancia_actual, ciudad_actual = heapq.heappop(cola_prioridad)

        if distancia_actual > distancias[ciudad_actual]:
            continue

        for vecino, peso in ciudad_actual.obtener_vecinos():
            distancia = distancia_actual + peso

            if distancia < distancias.get(vecino, float('inf')):
                distancias[vecino] = distancia
                ciudades_previas[vecino] = ciudad_actual
                heapq.heappush(cola_prioridad, (distancia, vecino))

    return distancias, ciudades_previas

def get_shortest_path(start_city, end_city):
    distances, previous_cities = dijkstra(start_city)
    path = []
    city = end_city

    while previous_cities[city]:
        path.insert(0, city)
        city = previous_cities[city]
    path.insert(0, city)

    return path, distances[end_city]

class ArbolBinarioBusqueda:

    def __init__(self):
        self.raiz = None
        self.tamano = 0

    def agregar(self,clave,valor):
        if self.raiz:
            self._agregar(clave,valor,self.raiz)
        else:
            self.raiz = NodoArbol(clave,valor)
        self.tamano = self.tamano + 1

    def _agregar(self,clave,valor,nodoActual):
        if clave < nodoActual.clave:
            if nodoActual.tieneHijoIzquierdo():
                self._agregar(clave,valor,nodoActual.hijoIzquierdo)
            else:
                nodoActual.hijoIzquierdo = NodoArbol(clave,valor,padre=nodoActual)
        else:
            if nodoActual.tieneHijoDerecho():
                self._agregar(clave,valor,nodoActual.hijoDerecho)
            else:
                nodoActual.hijoDerecho = NodoArbol(clave,valor,padre=nodoActual)

    def __setitem__(self,c,v):
        self.agregar(c,v)

    def obtener(self,clave):
        if self.raiz:
            res = self._obtener(clave,self.raiz)
            if res:
                return res.cargaUtil
            else:
                return None
        else:
            return None

    def _obtener(self,clave,nodoActual):
        if not nodoActual:
            return None
        elif nodoActual.clave == clave:
            return nodoActual
        elif clave < nodoActual.clave:
            return self._obtener(clave,nodoActual.hijoIzquierdo)
        else:
            return self._obtener(clave,nodoActual.hijoDerecho)
    
    def obtener_claves(self):
        claves = []
        self._obtener_claves(self.raiz, claves)
        return claves

    def _obtener_claves(self, nodoActual, claves):
        if nodoActual:
            self._obtener_claves(nodoActual.hijoIzquierdo, claves)  # Recorrer el hijo izquierdo
            claves.append(nodoActual.clave)  # Añadir la clave del nodo actual
            self._obtener_claves(nodoActual.hijoDerecho, claves)  # Recorrer el hijo derecho

    def obtener_lista(self):
        return [self.obtener(clave) for clave in self.obtener_claves()]

    def __getitem__(self,clave): #define el método __getitem__ que toma un argumento clave.
        res = self.obtener(clave) #Llama al método obtener del objeto self con la clave proporcionada y almacena el resultado en res.
        if res: #Comprueba si res no es None o no está vacío.
            return res #Comprueba si res no es None o no está vacío.
        else:
            raise KeyError('Error, la clave no está en el árbol') #Si res es None o está vacío, lanza una excepción KeyError con el mensaje "Error, la clave no está en el árbol".

    def __contains__(self,clave):
        if self._obtener(clave,self.raiz):
            return True
        else:
            return False

    def longitud(self):
        return self.tamano

    def __len__(self):
        return self.tamano

    def __iter__(self):
        return self.raiz.__iter__()

    def eliminar(self,clave):
        if self.tamano > 1:
            nodoAEliminar = self._obtener(clave,self.raiz)
            if nodoAEliminar:
                self.remover(nodoAEliminar)
                self.tamano = self.tamano-1
            else:
                raise KeyError('Error, la clave no está en el árbol')
        elif self.tamano == 1 and self.raiz.clave == clave:
            self.raiz = None
            self.tamano = self.tamano - 1
        else:
            raise KeyError('Error, la clave no está en el árbol')

    def __delitem__(self,clave):
        self.eliminar(clave)

    def remover(self,nodoActual): #Define la función remover que toma como parámetros self y nodoActual.
        if nodoActual.esHoja(): #Verifica si el nodoActual es una hoja
            if nodoActual == nodoActual.padre.hijoIzquierdo: #Comprueba si nodoActual es el hijo izquierdo de su padre.
                nodoActual.padre.hijoIzquierdo = None #Si es el hijo izquierdo, elimina la referencia del padre al nodoActual
            else: #Si no es el hijo izquierdo, entonces es el hijo derecho.
                nodoActual.padre.hijoDerecho = None #Elimina la referencia del padre al nodoActual si es el hijo derecho.
        elif nodoActual.tieneAmbosHijos(): #Comprueba si el nodoActual tiene ambos hijos (izquierdo y derecho).
            suc = nodoActual.encontrarSucesor() #Encuentra el sucesor del nodoActual.
            suc.empalmar() #Reconecta los hijos del sucesor (suc) con el árbol.
            nodoActual.clave = suc.clave #Reemplaza la clave del nodoActual con la clave del sucesor.
            nodoActual.cargaUtil = suc.cargaUtil #Reemplaza la carga útil del nodoActual con la carga útil del sucesor.

        else: # este nodo tiene un (1) hijo
            if nodoActual.tieneHijoIzquierdo(): #Verifica si el nodoActual tiene un hijo izquierdo.
                if nodoActual.esHijoIzquierdo(): #Comprueba si nodoActual es el hijo izquierdo de su padre.
                    nodoActual.hijoIzquierdo.padre = nodoActual.padre #Establece el padre del hijo izquierdo del nodoActual al padre del nodoActual.
                    nodoActual.padre.hijoIzquierdo = nodoActual.hijoIzquierdo #Reemplaza el nodoActual por su hijo izquierdo en su padre.
                elif nodoActual.esHijoDerecho(): #Si no es el hijo izquierdo, comprueba si es el hijo derecho.
                    nodoActual.hijoIzquierdo.padre = nodoActual.padre #Establece el padre del hijo izquierdo del nodoActual al padre del nodoActual.
                    nodoActual.padre.hijoDerecho = nodoActual.hijoIzquierdo #Reemplaza el nodoActual por su hijo izquierdo en su padre.
                else: #Si nodoActual no es ni hijo izquierdo ni derecho (es decir, es la raíz).
                    nodoActual.reemplazarDatoDeNodo(nodoActual.hijoIzquierdo.clave, nodoActual.hijoIzquierdo.cargaUtil, nodoActual.hijoIzquierdo.hijoIzquierdo, nodoActual.hijoIzquierdo.hijoDerecho) #Reemplaza los datos del nodoActual con los del hijo izquierdo.
            else: #Si el nodoActual no tiene un hijo izquierdo (tiene solo un hijo derecho).
                if nodoActual.esHijoIzquierdo(): #Comprueba si nodoActual es el hijo izquierdo de su padre.
                    nodoActual.hijoDerecho.padre = nodoActual.padre#Establece el padre del hijo derecho del nodoActual al padre del nodoActual.
                    nodoActual.padre.hijoIzquierdo = nodoActual.hijoDerecho#Reemplaza el nodoActual por su hijo derecho en su padre.
                elif nodoActual.esHijoDerecho(): #Si no es el hijo izquierdo, comprueba si es el hijo derecho.
                    nodoActual.hijoDerecho.padre = nodoActual.padre #Establece el padre del hijo derecho del nodoActual al padre del nodoActual.
                    nodoActual.padre.hijoDerecho = nodoActual.hijoDerecho #Reemplaza el nodoActual por su hijo derecho en su padre.
                else: # Si nodoActual no es ni hijo izquierdo ni derecho (es decir, es la raíz).
                    nodoActual.reemplazarDatoDeNodo(nodoActual.hijoDerecho.clave, nodoActual.hijoDerecho.cargaUtil, nodoActual.hijoDerecho.hijoIzquierdo, nodoActual.hijoDerecho.hijoDerecho) # Reemplaza los datos del nodoActual con los del hijo derecho.

    def inorden(self):
        self._inorden(self.raiz)

    def _inorden(self,arbol):
        if arbol != None:
            self._inorden(arbol.hijoIzquierdo)
            print(arbol.clave)
            self._inorden(arbol.hijoDerecho)

    def postorden(self):
        self._postorden(self.raiz)

    def _postorden(self, arbol):
        if arbol:
            self._postorden(arbol.hijoDerecho)
            self._postorden(arbol.hijoIzquierdo)
            print(arbol.clave)

    def preorden(self):
        self._preorden(self.raiz)

    def _preorden(self,arbol):
        if arbol:
            print(arbol.clave)
            self._preorden(arbol.hijoIzquierdo)
            self._preorden(arbol.hijoDerecho)

class NodoArbol:
    def __init__(self,clave,valor,izquierdo=None,derecho=None,padre=None):
        self.clave = clave
        self.cargaUtil = valor
        self.hijoIzquierdo = izquierdo
        self.hijoDerecho = derecho
        self.padre = padre
        self.factorEquilibrio = 0

    def tieneHijoIzquierdo(self):
        return self.hijoIzquierdo

    def tieneHijoDerecho(self):
        return self.hijoDerecho

    def esHijoIzquierdo(self):
        return self.padre and self.padre.hijoIzquierdo == self

    def esHijoDerecho(self):
        return self.padre and self.padre.hijoDerecho == self

    def esRaiz(self):
        return not self.padre

    def esHoja(self):
        return not (self.hijoDerecho or self.hijoIzquierdo)

    def tieneAlgunHijo(self):
        return self.hijoDerecho or self.hijoIzquierdo

    def tieneAmbosHijos(self):
        return self.hijoDerecho and self.hijoIzquierdo

    def reemplazarDatoDeNodo(self,clave,valor,hizq,hder):
        self.clave = clave
        self.cargaUtil = valor
        self.hijoIzquierdo = hizq
        self.hijoDerecho = hder
        if self.tieneHijoIzquierdo():
            self.hijoIzquierdo.padre = self
        if self.tieneHijoDerecho():
            self.hijoDerecho.padre = self

    def encontrarSucesor(self):
        suc = None
        if self.tieneHijoDerecho():
            suc = self.hijoDerecho.encontrarMin()
        else:
            if self.padre:
                if self.esHijoIzquierdo():
                    suc = self.padre
                else:
                    self.padre.hijoDerecho = None
                    suc = self.padre.encontrarSucesor()
                    self.padre.hijoDerecho = self
        return suc

    def empalmar(self):
        if self.esHoja():
            if self.esHijoIzquierdo():
                self.padre.hijoIzquierdo = None
            else:
                self.padre.hijoDerecho = None
        elif self.tieneAlgunHijo():
            if self.tieneHijoIzquierdo():
                if self.esHijoIzquierdo():
                    self.padre.hijoIzquierdo = self.hijoIzquierdo
                else:
                    self.padre.hijoDerecho = self.hijoIzquierdo
                self.hijoIzquierdo.padre = self.padre
            else:
                if self.esHijoIzquierdo():
                    self.padre.hijoIzquierdo = self.hijoDerecho
                else:
                    self.padre.hijoDerecho = self.hijoDerecho
                self.hijoDerecho.padre = self.padre

    def encontrarMin(self):
        actual = self
        while actual.tieneHijoIzquierdo():
            actual = actual.hijoIzquierdo
        return actual

    def __iter__(self):
        if self:
            if self.tieneHijoIzquierdo():
                for elem in self.hijoIzquierdo:
                    yield elem
            yield self.clave
            if self.tieneHijoDerecho():
                for elem in self.hijoDerecho:
                    yield elem