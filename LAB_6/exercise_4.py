"""
Zadanie 4:
Dany jest graf nieskierowany, nieważony. Niech długość ścieżki będzie liczbą krawędzi na niej.
Zaimplementuj rekurencyjną metodę wyznaczania najkrótszej ścieżki między dwoma zadanymi wierzchołkami.
Jeśli wierzchołki nie są bezpośrednimi sąsiadami, metoda wywołuje się rekurencyjnie, na każdym z bezpośrednich sąsiadów pierwszego wierzchołka i na drugim wierzchołku.
Jeśli wierzchołki są bezpośrednimi sąsiadami zwracana odległość to 1.
Uwaga: zadbaj o to, żeby wierzchołków nie odwiedzać wielokrotnie i o to, żeby algorytm nie zapętlał się w
nieskończoność (a dokładniej, do przepełnienia stosu).
Wejście: graf zadany w pliku (zaproponuj format pliku).
Wyjście: najkrótsza ścieżka i jej długość.
Oszacuj złożoność czasową algorytmu.
"""

import networkx as nx


def min_path(G, u, v, visited=None):
    if visited is None:
        visited = set()
    if u == v:
        return 0
    visited.add(u)
    min_path_length = float('inf')
    for neighbor in G[u]:
        if neighbor not in visited:
            path_length = 1 + min_path(G, neighbor, v, visited)
            min_path_length = min(min_path_length, path_length)
    visited.remove(u)
    return min_path_length


G = nx.Graph()
G.add_edges_from([(0, 1), (0, 2),(1,2), (1, 3), (2, 4), (4, 5), (1, 5)])

u = 1
v = 5
path_length = min_path(G, u, v)
print(f"Minimalna długość ścieżki między wierzchołkami {u} i {v}: {path_length}")