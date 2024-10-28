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

class ArbolBinarioBusqueda: # Se define el objeto de clase ArbolBinarioBusqueda

    def __init__(self): # Se define el constructor del objeto con el parametro self
        self.raiz = None # Se crea un atributo raiz con valor None
        self.tamano = 0 # Se crea un atributo tamano con valor 0

    def agregar(self,clave,valor): # Se define el metodo agregar con los parametros self, clave y valor
        if self.raiz: # Si el atributo raiz no es None ingresa al if
            self._agregar(clave,valor,self.raiz) # Accede al metodo _agregar pasandole como parametros clave, valor y raiz
        else: # En caso de que el atributo raiz sea None, ingresa al else
            self.raiz = NodoArbol(clave,valor) # Raiz ahora va a almacenar un objeto de clase NodoArbol y le pasa los parametros clave y valor
        self.tamano = self.tamano + 1 # Se incrementa el tamaño de tamano a +1

    def _agregar(self,clave,valor,nodoActual): # Se define el metodo _agregar con los parametros self, clave, valor y nodoActual
        if clave < nodoActual.clave: # Compara si el valor del parametro clave es menor al valor de la clave del parametro nodoActual. Si es True ingresa al if
            if nodoActual.tieneHijoIzquierdo(): # Verifica si el nodoActual tiene un hijo izquierdo con el metodo tieneHijoIzquierdo de la clase NodoArbol. Si da true ingresa al if
                self._agregar(clave,valor,nodoActual.hijoIzquierdo) # Se llama de nuevo al metodo _agregar con los parametros clave, valor y el hijo izquierdo del nodoActual 
            else: # Si el nodoActual no tiene hijo izquierdo ingresa al else
                nodoActual.hijoIzquierdo = NodoArbol(clave,valor,padre=nodoActual) # Se le define el valor del hijo izquierdo del nodoActual con un nuevo nodo, donde se le pasa la clave, valor; y padre no va a ser None, sino el nodoActual 
        else: # Si la clave es igual o mayor que la clave del nodoActual ingresa al else
            if nodoActual.tieneHijoDerecho(): # Verifica si el nodoActual tiene un hijo derecho con el metodo tieneHijoDerecho de la clase NodoArbol. Si da true ingresa al if
                self._agregar(clave,valor,nodoActual.hijoDerecho) # Se llama de nuevo al metodo _agregar con los parametros clave, valor y el hijo derecho del nodoActual
            else: # Si el nodoActual no tiene hijo derecho ingresa al else
                nodoActual.hijoDerecho = NodoArbol(clave,valor,padre=nodoActual) # Se le define el valor del hijo derecho del nodoActual con un nuevo nodo, donde se le pasa la clave, valor; y padre no va a ser None, sino el nodoActual

    def __setitem__(self,c,v): # Se define el metodo __setitem__ con los parametros self, c y v
        self.agregar(c,v) # Se invoca al metodo agregar pasandole los valores c y v (clave y valor)

    def obtener(self,clave): # Se define el metodo obtener con los parametros self y clave
        if self.raiz: # Si la raiz no es None, ingresa al if
            res = self._obtener(clave,self.raiz) # Se llama al metodo _obtener pasandole como parametros clave y self.raiz, y esto se guarda en la variable res
            if res: # Si hay algun valor que no sea None en res, ingresa al if
                return res.cargaUtil # Retorna el valor guardado en cargaUtil de la variable res
            else: # Si no hay algun valor en la variable res ingresa al else
                return None # Retorna None
        else: # Si la condicion de la linea 67 no se cumple, ingresa al else
            return None # Retorna None

    def _obtener(self,clave,nodoActual): # Se define el metodo _obtener con los parametros self, clave y nodoActual
        if not nodoActual: # Compara si no hay un nodo en el parametro nodoActual. Si da True ingresa al if
            return None # Retorna None
        elif nodoActual.clave == clave: # Si no se cumple el if anterior pero la clave de nodoActual es igual al valor del parametro de clave, ingresa al elif
            return nodoActual # Retorna el nodo que se encuentra en el parametro nodoActual
        elif clave < nodoActual.clave: # Si no se cumple el elif anterior pero el valor del parametro clave es menor a la clave del nodoActual, ingresa a este nuevo elif
            return self._obtener(clave,nodoActual.hijoIzquierdo) # Se hace una recursion del metodo _obtener donde retorna los parametros clave y el nuevo valor de nodoActual que es el hijo izquierdo del mismo
        else: # Si no se cumple ninguna de las condiciones anteriores, ingresa al else
            return self._obtener(clave,nodoActual.hijoDerecho) # Se hace una recursion del metodo _obtener donde retorna los parametros clave y el nuevo valor de nodoActual que es el hijo derecho del mismo
    
    def obtener_claves(self): # Se define el metodo obtener_claves con el parametro self
        claves = [] # Se define una lista vacia dentro de la variable claves
        self._obtener_claves(self.raiz, claves) # Se llama al metodo _obtener_claves donde se pasan como parametros self.raiz y claves
        return claves # Retorna el valor almacenado en el parametro claves

    def _obtener_claves(self, nodoActual, claves): # Se define el metodo _obtener_claves con los parametro self, nodoActual y claves
        if nodoActual: # Si hay un valor en el parametro nodoActual, ingresa al if 
            self._obtener_claves(nodoActual.hijoIzquierdo, claves)  # Recorrer el hijo izquierdo
            claves.append(nodoActual.clave)  # Añadir la clave del nodo actual
            self._obtener_claves(nodoActual.hijoDerecho, claves)  # Recorrer el hijo derecho

    def obtener_lista(self): # Se define el metodo obtener_lista con el parametro self
        return [self.obtener(clave) for clave in self.obtener_claves()] #!

    def __getitem__(self,clave): # Se define el metodo __getitem__ con los parametros self y clave
        res = self.obtener(clave) # Llama al metodo obtener con el parametro clave y guarda el resultado en la variable res
        if res: # Comprueba si res no es None. Si da True ingresa al if
            return res # Retorna el valor almacenado en la variable res
        else: # Si la variable res tiene como valor None, ingresa al else 
            raise KeyError('Error, la clave no está en el árbol') # Lanza una excepción KeyError con el mensaje "Error, la clave no está en el árbol"

    def __contains__(self,clave): # Se define el metodo __contains__ con los parametros self y clave
        if self._obtener(clave,self.raiz): # Se invoca al metodo _obtener y se le pasa como parametros clave y la raiz del objeto self. Si hay algun valor, ingresa al if
            return True # Retorna True
        else: # Si la condicion anterior obtiene como valor None, ingresa al else
            return False # Retorna False

    def longitud(self): # Se define el metodo longitud con el parametro self
        return self.tamano # Retorna el valor guardado en tamano del objeto self

    def __len__(self): # Se define el metodo __len__ con el parametro self
        return self.tamano # Retorna el valor guardado en tamano del objeto self

    def __iter__(self): # Se define el metodo __iter__ con el parametro self
        return self.raiz.__iter__() # Retorna el valor guardado en raiz del objeto self y lo hace iterable con el metodo __iter__

    def eliminar(self,clave): # Se define el metodo eliminar con los parametros self y clave
        if self.tamano > 1: # Si el tamaño del árbol es mayor que 1, hay más de un nodo en el árbol
            nodoAEliminar = self._obtener(clave,self.raiz) # Busca el nodo a eliminar usando el método _obtener, comenzando desde la raíz
            if nodoAEliminar: # Si se encuentra el nodo con la clave especificada
                self.remover(nodoAEliminar) # Llama al método remover para eliminar el nodo encontrado
                self.tamano = self.tamano-1 # Reduce el tamaño del árbol en 1
            else: # Si no se encuentra el nodo entra al else
                raise KeyError('Error, la clave no está en el árbol') # Lanza una excepción KeyError con el mensaje "Error, la clave no está en el árbol"
        elif self.tamano == 1 and self.raiz.clave == clave: # Si el tamaño del árbol es igual a 1 y la raíz es el nodo con la clave especificada
            self.raiz = None # Elimina el único nodo del árbol estableciendo la raíz a None
            self.tamano = self.tamano - 1 # Reduce el tamaño del árbol en 1
        else: # Si ninguna de las condiciones anteriores se cumple
            raise KeyError('Error, la clave no está en el árbol') # Lanza una excepción KeyError con el mensaje "Error, la clave no está en el árbol"

    def __delitem__(self,clave): # Se define el metodo __delitem__ con los parametros self y clave
        self.eliminar(clave) # Se invoca al metodo eliminar del objeto self donde se le pasa como parametro clave

    def remover(self,nodoActual): # Se define el metodo remover que toma como parámetros self y nodoActual
        if nodoActual.esHoja(): # Verifica si el nodoActual es una hoja
            if nodoActual == nodoActual.padre.hijoIzquierdo: # Comprueba si nodoActual es el hijo izquierdo de su padre
                nodoActual.padre.hijoIzquierdo = None # Si es el hijo izquierdo, elimina la referencia del padre al nodoActual
            else: # Si no es el hijo izquierdo, entonces es el hijo derecho
                nodoActual.padre.hijoDerecho = None # Elimina la referencia del padre al nodoActual si es el hijo derecho
        elif nodoActual.tieneAmbosHijos(): # Comprueba si el nodoActual tiene ambos hijos (izquierdo y derecho)
            suc = nodoActual.encontrarSucesor() # Encuentra el sucesor del nodoActual
            suc.empalmar() # Reconecta los hijos del sucesor (suc) con el árbol
            nodoActual.clave = suc.clave # Reemplaza la clave del nodoActual con la clave del sucesor
            nodoActual.cargaUtil = suc.cargaUtil # Reemplaza la carga útil del nodoActual con la carga útil del sucesor

        else: # este nodo tiene un (1) hijo
            if nodoActual.tieneHijoIzquierdo(): # Verifica si el nodoActual tiene un hijo izquierdo
                if nodoActual.esHijoIzquierdo(): # Comprueba si nodoActual es el hijo izquierdo de su padre
                    nodoActual.hijoIzquierdo.padre = nodoActual.padre # Establece el padre del hijo izquierdo del nodoActual al padre del nodoActual
                    nodoActual.padre.hijoIzquierdo = nodoActual.hijoIzquierdo # Reemplaza el nodoActual por su hijo izquierdo en su padre
                elif nodoActual.esHijoDerecho(): # Si no es el hijo izquierdo, comprueba si es el hijo derecho
                    nodoActual.hijoIzquierdo.padre = nodoActual.padre # Establece el padre del hijo izquierdo del nodoActual al padre del nodoActual
                    nodoActual.padre.hijoDerecho = nodoActual.hijoIzquierdo # Reemplaza el nodoActual por su hijo izquierdo en su padre
                else: # Si nodoActual no es ni hijo izquierdo ni derecho (es decir, es la raíz)
                    nodoActual.reemplazarDatoDeNodo(nodoActual.hijoIzquierdo.clave, nodoActual.hijoIzquierdo.cargaUtil, nodoActual.hijoIzquierdo.hijoIzquierdo, nodoActual.hijoIzquierdo.hijoDerecho) # Reemplaza los datos del nodoActual con los del hijo izquierdo
            else: # Si el nodoActual no tiene un hijo izquierdo (tiene solo un hijo derecho)
                if nodoActual.esHijoIzquierdo(): # Comprueba si nodoActual es el hijo izquierdo de su padre
                    nodoActual.hijoDerecho.padre = nodoActual.padre # Establece el padre del hijo derecho del nodoActual al padre del nodoActual
                    nodoActual.padre.hijoIzquierdo = nodoActual.hijoDerecho # Reemplaza el nodoActual por su hijo derecho en su padre
                elif nodoActual.esHijoDerecho(): # Si no es el hijo izquierdo, comprueba si es el hijo derecho
                    nodoActual.hijoDerecho.padre = nodoActual.padre # Establece el padre del hijo derecho del nodoActual al padre del nodoActual
                    nodoActual.padre.hijoDerecho = nodoActual.hijoDerecho # Reemplaza el nodoActual por su hijo derecho en su padre
                else: # Si nodoActual no es ni hijo izquierdo ni derecho (es decir, es la raíz)
                    nodoActual.reemplazarDatoDeNodo(nodoActual.hijoDerecho.clave, nodoActual.hijoDerecho.cargaUtil, nodoActual.hijoDerecho.hijoIzquierdo, nodoActual.hijoDerecho.hijoDerecho) # Reemplaza los datos del nodoActual con los del hijo derecho

    def inorden(self): # Se define el metodo inorden con el parametro self
        self._inorden(self.raiz) # Llama al método _inorden comenzando desde la raíz del árbol

    def _inorden(self,arbol): # Se define el metodo _inorden con los parametros self y arbol
        if arbol != None: # Si el nodo actual no es None
            self._inorden(arbol.hijoIzquierdo) # Llama recursivamente al método _inorden para el subárbol izquierdo
            print(arbol.clave) # Imprime la clave del nodo actual
            self._inorden(arbol.hijoDerecho) # Llama recursivamente al método _inorden para el subárbol derecho

    def postorden(self): # Se define el metodo postorden con el parametro self
        self._postorden(self.raiz) # Llama al método _postorden comenzando desde la raíz del árbol

    def _postorden(self, arbol): # Se define el metodo _postorden con los parametros self y arbol
        if arbol: # Si el nodo actual no es None
            self._postorden(arbol.hijoIzquierdo) # Llama recursivamente al método _postorden para el subárbol izquierdo
            self._postorden(arbol.hijoDerecho) # Llama recursivamente al método _postorden para el subárbol derecho
            print(arbol.clave) # Imprime la clave del nodo actual

    def preorden(self): # Se define el metodo preorden con el parametro self
        self._preorden(self.raiz) # Llama al método _preorden comenzando desde la raíz del árbol

    def _preorden(self,arbol): # Se define el metodo _preorden con los parametros self y arbol
        if arbol: # Si el nodo actual no es None
            print(arbol.clave) # Imprime la clave del nodo actual 
            self._preorden(arbol.hijoIzquierdo) # Llama recursivamente al método _preorden para el subárbol izquierdo
            self._preorden(arbol.hijoDerecho) # Llama recursivamente al método _preorden para el subárbol derecho

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