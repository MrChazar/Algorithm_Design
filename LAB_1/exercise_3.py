import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
"""
Napisz program wyświetlający graf pełny o parametrach:
• liczba wierzchołków jest zadana parametrycznie (należy zapytać użytkownika, np. z poziomu konsoli),
• wierzchołki są rozmieszczone na okręgu, w równych odstępach między kolejnymi wierzchołkami,
• etykiety wierzchołkow są kolejnymi liczbami naturalnymi.
Procedurę umieszczania wierzchołków na okręgu przygotuj samodzielnie. Wykorzystaj odpowiednie funkcje
trygonometryczne.
Wejście: liczba wierzchołków.
Wyjście: wyświetlony graf.

"""
# Ustawianie Parametrów
number_of_vertices = 4

# Tworzenie wierzchołków
VV = [a for a in range(1, number_of_vertices+1)]
# Tworzenie krawędzi grafu pełnego
WW = [(a, b) for a in VV for b in VV if a != b]
WW.append((number_of_vertices, 1))
# Tworzenie pozycji wierzchołków w kształcie okręgu
pos = {}
Vx = {a: np.cos(2*np.pi*a)/number_of_vertices for a in VV}
Vy = {a: np.sin(2*np.pi*a)/number_of_vertices for a in VV}
for v in VV:
    pos[v] = [Vx[v], Vy[v]]

g = nx.Graph()

for v in VV:
    g.add_node(v)
    for v1 in VV:
        for v2 in VV:
            if (v1, v2) in WW:
                g.add_edge(v1, v2)
# make circle positions
nx.draw(g, with_labels=True, node_color="yellow")
labels = nx.get_edge_attributes(g, "weight")
nx.draw_networkx_edge_labels(g, edge_labels=labels, pos=pos)
plt.show()
