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