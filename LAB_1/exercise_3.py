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
number_of_vertices = 10

# Tworzenie wierzchołków
VV = [a for a in range(1, number_of_vertices+1)]
# Tworzenie krawędzi grafu pełnego
WW = [(a, b) for a in VV for b in VV if a != b]
WW.append((number_of_vertices, 1))
# Tworzenie pozycji wierzchołków w kształcie okręgu
pos = {}
step = 2*np.pi/number_of_vertices

# Tworzenie grafu
g = nx.Graph()
for v in VV:
    g.add_node(v)
    pos[v] = [np.sin(VV.index(v) * step), np.cos(VV.index(v) * step)]
for v1 in VV:
        for v2 in VV:
            if v1 == v2:
                continue
            g.add_edges_from([(v1, v2)])

# Rysowanie Grafu
nx.draw(g, pos, with_labels=True)
plt.show()

