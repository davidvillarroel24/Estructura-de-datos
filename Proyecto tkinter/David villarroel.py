import tkinter as tk
from tkinter import ttk, messagebox

class Producto:
    def __init__(self, id, nombre, precio, cantidad):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Precio: ${self.precio:.2f}, Cantidad: {self.cantidad}"

class Inventario:
    def __init__(self):        
        self.productos = ListaEnlazada()

    def agregar_producto(self, producto):        

        ######################################################################################        
        actual = self.productos.inicio
            # Recorrer la lista y mostrar cada dato                    
        while actual:
            #print(actual.dato, end=" -> ")
            if producto.id == actual.dato.id:
                actual.dato.cantidad += producto.cantidad
                return 
            actual = actual.siguiente

        self.productos.agregar(producto)


    def eliminar_producto(self, id):

        actual = self.productos.inicio
            # Recorrer la lista y mostrar cada dato                    
        while actual:
            #print(actual.dato, end=" -> ")
            if id == actual.dato.id:
                self.productos.eliminar(actual.dato)
                return True                
            actual = actual.siguiente
        return False              

        """ if id in self.productos:
            del self.productos[id]
            return True
        return False """

    def actualizar_producto(self, id, nombre, precio, cantidad):
    
        actual = self.productos.inicio
            # Recorrer la lista y mostrar cada dato                    
        while actual:
            #print(actual.dato, end=" -> ")
            if id == actual.dato.id:
                actual.dato.nombre=nombre
                actual.dato.precio=precio
                actual.cantidad=cantidad                
                """ self.productos.eliminar(actual.dato)"""
                return True                 
            actual = actual.siguiente
        return False  
    
    """  if id in self.productos:
        self.productos[id].nombre = nombre
        self.productos[id].precio = precio
        self.productos[id].cantidad = cantidad
        return True
    return False """

    def buscar_producto(self, id):
        return self.productos.get(id)

    def listar_productos(self):
        return list(self.productos.values())

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




class InventarioApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Gestión de Inventario")
        self.root.geometry("800x600")
        self.inventario = Inventario()
        

        self.style = ttk.Style()
        self.style.configure('TButton', font=('Arial', 10), padding=5)
        self.style.configure('TLabel', font=('Arial', 10))
        self.style.configure('TEntry', font=('Arial', 10))
        

        self.create_widgets()
        
    
        self.inventario.agregar_producto(Producto(1, "Laptop", 1200.00, 10))
        self.inventario.agregar_producto(Producto(2, "Mouse", 25.50, 50))
        self.actualizar_lista()

    def create_widgets(self):
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        input_frame = ttk.LabelFrame(main_frame, text="Datos del Producto")
        input_frame.grid(row=0, column=0, sticky="ew", padx=5, pady=5)

        ttk.Label(input_frame, text="ID:").grid(row=0, column=0, padx=5, pady=5)
        self.id_entry = ttk.Entry(input_frame)
        self.id_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(input_frame, text="Nombre:").grid(row=1, column=0, padx=5, pady=5)
        self.nombre_entry = ttk.Entry(input_frame)
        self.nombre_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(input_frame, text="Precio:").grid(row=2, column=0, padx=5, pady=5)
        self.precio_entry = ttk.Entry(input_frame)
        self.precio_entry.grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(input_frame, text="Cantidad:").grid(row=3, column=0, padx=5, pady=5)
        self.cantidad_entry = ttk.Entry(input_frame)
        self.cantidad_entry.grid(row=3, column=1, padx=5, pady=5)

        btn_frame = ttk.Frame(input_frame)
        btn_frame.grid(row=4, columnspan=2, pady=10)

        ttk.Button(btn_frame, text="Agregar", command=self.agregar_producto).grid(row=0, column=0, padx=5)
        ttk.Button(btn_frame, text="Actualizar", command=self.actualizar_producto).grid(row=0, column=1, padx=5)
        ttk.Button(btn_frame, text="Eliminar", command=self.eliminar_producto).grid(row=0, column=2, padx=5)
        ttk.Button(btn_frame, text="Buscar", command=self.buscar_producto).grid(row=0, column=3, padx=5)
        ttk.Button(btn_frame, text="Limpiar", command=self.limpiar_campos).grid(row=0, column=4, padx=5)

        list_frame = ttk.LabelFrame(main_frame, text="Productos en Inventario")
        list_frame.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)

        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(1, weight=1)

        columns = ("id", "nombre", "precio", "cantidad")
        self.tree = ttk.Treeview(list_frame, columns=columns, show="headings")
        

        self.tree.heading("id", text="ID")
        self.tree.heading("nombre", text="Nombre")
        self.tree.heading("precio", text="Precio")
        self.tree.heading("cantidad", text="Cantidad")
        
        self.tree.column("id", width=50)
        self.tree.column("nombre", width=200)
        self.tree.column("precio", width=100)
        self.tree.column("cantidad", width=100)
        
        self.tree.pack(fill=tk.BOTH, expand=True)
        
        scrollbar = ttk.Scrollbar(list_frame, orient="vertical", command=self.tree.yview)
        scrollbar.pack(side="right", fill="y")
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        self.tree.bind("<ButtonRelease-1>", self.seleccionar_producto)

    def agregar_producto(self):
        try:
            id = int(self.id_entry.get())
            nombre = self.nombre_entry.get()
            precio = float(self.precio_entry.get())
            cantidad = int(self.cantidad_entry.get())
            
            producto = Producto(id, nombre, precio, cantidad)
            self.inventario.agregar_producto(producto)
            self.actualizar_lista()
            self.limpiar_campos()
            messagebox.showinfo("Éxito", "Producto agregado correctamente")
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese valores válidos")

    def actualizar_producto(self):
        try:
            id = int(self.id_entry.get())
            nombre = self.nombre_entry.get()
            precio = float(self.precio_entry.get())
            cantidad = int(self.cantidad_entry.get())
            
            if self.inventario.actualizar_producto(id, nombre, precio, cantidad):
                self.actualizar_lista()
                messagebox.showinfo("Éxito", "Producto actualizado correctamente")
            else:
                messagebox.showerror("Error", "Producto no encontrado")
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese valores válidos")

    def eliminar_producto(self):
        try:
            id = int(self.id_entry.get())
            if self.inventario.eliminar_producto(id):
                self.actualizar_lista()
                messagebox.showinfo("Éxito", "Producto eliminado correctamente")
            else:
                messagebox.showerror("Error", "Producto no encontrado")
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese un ID válido")

    def buscar_producto(self):
        try:
            id = int(self.id_entry.get())
            producto = self.inventario.buscar_producto(id)
            if producto:
                self.nombre_entry.delete(0, tk.END)
                self.precio_entry.delete(0, tk.END)
                self.cantidad_entry.delete(0, tk.END)
                
                self.nombre_entry.insert(0, producto.nombre)
                self.precio_entry.insert(0, str(producto.precio))
                self.cantidad_entry.insert(0, str(producto.cantidad))
            else:
                messagebox.showinfo("No encontrado", "Producto no encontrado")
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese un ID válido")

    def seleccionar_producto(self, event):
        selected_item = self.tree.focus()
        if selected_item:
            values = self.tree.item(selected_item, "values")
            if values:
                self.id_entry.delete(0, tk.END)
                self.nombre_entry.delete(0, tk.END)
                self.precio_entry.delete(0, tk.END)
                self.cantidad_entry.delete(0, tk.END)
                
                self.id_entry.insert(0, values[0])
                self.nombre_entry.insert(0, values[1])
                self.precio_entry.insert(0, values[2])
                self.cantidad_entry.insert(0, values[3])

    def actualizar_lista(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        actual = self.inventario.productos.inicio

        while actual:
            self.tree.insert("", tk.END, values=(
                actual.dato.id, 
                actual.dato.nombre, 
                f"${actual.dato.precio:.2f}", 
                actual.dato.cantidad
            ))
            #print(actual.dato, end=" -> ")
            actual = actual.siguiente

        """ for producto in self.inventario.listar_productos():
            self.tree.insert("", tk.END, values=(
                producto.id, 
                producto.nombre, 
                f"${producto.precio:.2f}", 
                producto.cantidad
             ))"""

    def limpiar_campos(self):
        self.id_entry.delete(0, tk.END)
        self.nombre_entry.delete(0, tk.END)
        self.precio_entry.delete(0, tk.END)
        self.cantidad_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = InventarioApp(root)
    root.mainloop()
