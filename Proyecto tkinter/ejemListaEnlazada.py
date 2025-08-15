# Clase que representa un nodo de la lista enlazada
class Nodo: 
    def __init__(self, dato):
        self.dato = dato            # Almacena el dato del nodo
        self.siguiente = None       # Puntero al siguiente nodo (inicialmente es None)

# Clase que representa la lista enlazada
class ListaEnlazada:
    def __init__(self):
        self.inicio = None          # Referencia al primer nodo de la lista

    # Método para agregar un nuevo nodo al final de la lista
    def agregar(self, dato):  
        nuevo = Nodo(dato)          # Crear un nuevo nodo con el dato dado
        if not self.inicio:         # Si la lista está vacía
            self.inicio = nuevo     # El nuevo nodo es ahora el primero
        else: 
            actual = self.inicio
            # Recorrer la lista hasta llegar al último nodo
            while actual.siguiente:
                actual = actual.siguiente
            # Agregar el nuevo nodo al final
            actual.siguiente = nuevo

    # Método para mostrar todos los elementos de la lista
    def mostrar(self):
        actual = self.inicio
        # Recorrer la lista y mostrar cada dato
        while actual:
            print(actual.dato, end=" -> ")
            actual = actual.siguiente
        print("None")  # Indica el final de la lista

    # Método para eliminar un nodo que contenga un dato específico
    def eliminar(self, dato):
        actual = self.inicio
        anterior = None
        # Recorrer la lista buscando el nodo con el dato a eliminar
        while actual:
            if actual.dato == dato:
                if anterior:
                    # Si no es el primer nodo, conectar el nodo anterior con el siguiente
                    anterior.siguiente = actual.siguiente
                else:
                    # Si es el primer nodo, actualizar el inicio
                    self.inicio = actual.siguiente
                return  # Dato encontrado y eliminado, salir del método
            anterior = actual
            actual = actual.siguiente
        # Si no se encontró el dato, mostrar mensaje
        print("No se encontró el dato:", dato)

# Crear una lista enlazada y realizar algunas operaciones
lista = ListaEnlazada()
lista.agregar(1)         # Agrega el número 1 a la lista
lista.agregar(2)         # Agrega el número 2 a la lista
lista.agregar(3)         # Agrega el número 3 a la lista
lista.mostrar()          # Muestra: 1 -> 2 -> 3 -> None
lista.eliminar(2)        # Elimina el nodo con valor 2
lista.mostrar()          # Muestra: 1 -> 3 -> None
