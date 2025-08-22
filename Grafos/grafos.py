import networkx as nx
import matplotlib.pyplot as plt

grafos_no_dirigidos = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C"],
}

#crear un grafo no dirigido
G=nx.Graph()

for nodo,vecinos in grafos_no_dirigidos.items():
    for vecino in vecinos:
        G.add_edge(nodo, vecino)

# dibujar el grafo
plt.figure(num=1,figsize=(6,6))
nx.draw(G, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=16,font_weight='bold')
plt.title("Grafo No Dirigido",fontsize=20)
#plt.show()

amistades = [
    ("Ana","Bruno"),
    ("Ana","Caro"),
    ("Bruno","Diego"),
    ("Caro","Diego"),
    ("Caro","Elena"),    
]

# mostrar amigos de caro
#este add_edges_from permite agregar múltiples aristas al grafo
G2=nx.Graph()
G2.add_edges_from(amistades)

print("Amigos de Caro:", list(G2.neighbors("Caro")))

plt.figure(num=2,figsize=(6,6))
nx.draw(G2, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=16,font_weight='bold')
plt.title("Grafo No Dirigido",fontsize=20)

#ejericio 3
amistades = [
    ("Ana","Bruno"),
    ("Ana","Caro"),
    ("Ana","Fernando"),

    ("Bruno","Diego"),
    #("Bruno","Ana"),
    
    #("Diego","Bruno"),
    ("Diego","Caro"),
    ("Diego","Gabriela"),
    
    #("Gabriela","Diego"),
    ("Gabriela","Caro"),

    #("Caro","Diego"),
    #("Caro","Ana"),
    ("Caro","Elena"),    
    #("Caro","Gabriela"), 

    ("Elena","Caro"),
    ("Elena","Fernando"),

    #("Fernando","Ana"),
    ("Fernando","Elena"),

    ("Hugo","Fernando")
]

# mostrar amigos de caro
#este add_edges_from permite agregar múltiples aristas al grafo
G3=nx.Graph()
G3.add_edges_from(amistades)

print("Amigos de Caro:", list(G3.neighbors("Caro")))

plt.figure(num=3,figsize=(6,6))
nx.draw(G3, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=16,font_weight='bold')
plt.title("Grafo No Dirigido",fontsize=20)

#Ejericio 4
amistades = [
    ("Transf2","CasaD"),
    ("Transf2","CasaC"),
    ("Planta","Transf2"),
    ("Planta","Transf1"),    
    ("Transf1","CasaB"),
    ("Transf1","CasaA"),
]

# Que casas se apagan si falla transf1

# mostrar amigos de caro
#este add_edges_from permite agregar múltiples aristas al grafo
G4=nx.Graph()
G4.add_edges_from(amistades)

print("Casa afectadas:", list(G4.neighbors("Transf1")))

plt.figure(num=4,figsize=(6,6))
nx.draw(G4, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=16,font_weight='bold')
plt.title("Grafo No Dirigido",fontsize=20)
plt.show()
