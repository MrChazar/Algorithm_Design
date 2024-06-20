"""
Zadanie nr 5 – minimalne drzewo rozpinające
Dla zadanego grafu wczytywanego z pliku zaimplementuj algorytm Kruskala (generacji minimalnego drzewa
rozpinającego).
W implementacji wykorzystaj zbiory rozłączne.
Procedurę przedstaw graficznie, krok po kroku.
Wejście: plik z grafem, początkowy wierzchołek.
Wyjście: wizualizacja.
"""

import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import time


def load_graph(txt):
    adj_matrix = pd.read_csv(txt, delim_whitespace=True, header=None)
    G = nx.from_pandas_adjacency(adj_matrix, create_using=nx.Graph)
    return G


def draw_graph(graph, pos=None, mst_edges=None, added_edge=None):
    plt.figure(figsize=(8, 6))
    if pos is None:
        pos = nx.spring_layout(graph)
    nx.draw(graph, pos, with_labels=True, node_size=700, node_color="skyblue", edge_color='gray')
    if mst_edges:
        nx.draw_networkx_edges(graph, pos, edgelist=mst_edges, edge_color='green', width=2)
    if added_edge:
        nx.draw_networkx_edges(graph, pos, edgelist=[added_edge], edge_color='red', width=2)
    plt.show()


class DisjointSet:
    def __init__(self, nodes):
        self.parent = {node: node for node in nodes}
        self.rank = {node: 0 for node in nodes}

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)

        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            elif self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1


def kruskal_mst(graph):
    mst_edges = []
    edges = sorted(graph.edges(data=True), key=lambda x: x[2]['weight'])
    disjoint_set = DisjointSet(graph.nodes())
    pos = nx.spring_layout(graph)

    for edge in edges:
        node1, node2, weight = edge
        if disjoint_set.find(node1) != disjoint_set.find(node2):
            disjoint_set.union(node1, node2)
            mst_edges.append(edge)
            draw_graph(graph, pos, mst_edges=mst_edges, added_edge=edge)
            time.sleep(1)  # Opóźnienie dla lepszego efektu wizualnego

    return mst_edges


# Wczytanie grafu i wyświetlenie go
g = load_graph('data/graph.txt')
draw_graph(g)

# Przeprowadzenie algorytmu Kruskala i wizualizacja kroków
mst_edges = kruskal_mst(g)
print("Edges in MST:", mst_edges)
