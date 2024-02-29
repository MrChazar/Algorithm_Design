import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
"""
Napisz program wyświetlający graf pusty o parametrycznie zadanej liczbie wierzchołków (podawana przez
użytkownika). Wierzchołki są generowane na losowej pozycji na płaszczyźnie Oxy. Losowej, czyli losowanej z
rozkładów jednostajnych dla osi Ox i Oy na pewnych ustalonych przedziałach (podanych przez użytkownika).
Wyświetl uzyskany graf.
Wejście: liczba wierzchołków, przedział na osi Ox, przedział na osi Oy.
Wyjście: wyświetlony graf.
"""

# Ustawianie Parametrów
number_of_vertices = 100
uniform_distribution = (5, 1)

# Tworzenie wierzchołków
VV = [a for a in range(1, number_of_vertices+1)]

# Tworzenie grafu
pos = {}
g = nx.Graph()
for v in VV:
    g.add_node(v)
    pos[v] = [np.random.uniform(uniform_distribution[0], uniform_distribution[1]), np.random.uniform(uniform_distribution[0], uniform_distribution[1])]

# Rysowanie Grafu
nx.draw(g, pos, with_labels=True)
plt.show()