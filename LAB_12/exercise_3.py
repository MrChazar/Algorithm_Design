"""
Zadanie nr 3 – drzewo przeszukiwań w głąb
Uzupełnij poprzednie zadanie tak, aby kolorować krawędzie zgodnie z ich typem: drzewowa, powrotna, w
przód, poprzeczna.
Wejście: plik z grafem.
Wyjście: wizualizacja.
"""

import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import time

def load_graph(txt):
    adj_matrix = pd.read_csv(txt, delim_whitespace=True, header=None)
    G = nx.from_pandas_adjacency(adj_matrix, create_using=nx.DiGraph)
    return G

def draw_graph(graph, pos, visited_nodes, edge_colors):
    plt.figure(figsize=(8, 6))
    node_color = ['red' if node in visited_nodes else 'skyblue' for node in graph.nodes()]
    nx.draw(graph, pos, with_labels=True, node_size=700, node_color=node_color, edge_color=edge_colors, arrows=True)
    plt.show()

def classify_edge(u, v, graph, visited, entry, low, parent):
    if visited[v] == False:
        return 'tree'
    elif v != parent[u]:
        if entry[u] > entry[v]:
            return 'back'
        elif low[u] < entry[v]:
            return 'forward'
        else:
            return 'cross'

def traverse_full_dfs(graph):
    pos = nx.spring_layout(graph)
    visited = {node: False for node in graph.nodes()}
    parent = {node: None for node in graph.nodes()}
    entry = {node: float('inf') for node in graph.nodes()}
    low = {node: float('inf') for node in graph.nodes()}
    edge_colors = []

    time_counter = [0]
    traversal_order = []

    def dfs(u):
        visited[u] = True
        traversal_order.append(u)
        entry[u] = low[u] = time_counter[0]
        time_counter[0] += 1

        for v in graph.neighbors(u):
            edge_type = classify_edge(u, v, graph, visited, entry, low, parent)
            edge_colors.append((u, v, edge_type))
            if visited[v] == False:
                parent[v] = u
                dfs(v)
                low[u] = min(low[u], low[v])
            elif v != parent[u]:
                low[u] = min(low[u], entry[v])

            # Visualize step by step
            edge_colormap = {'tree': 'green', 'back': 'red', 'forward': 'blue', 'cross': 'yellow'}
            edge_colors_mapped = [edge_colormap[etype] for (_, _, etype) in edge_colors]
            draw_graph(graph, pos, visited, edge_colors_mapped)
            time.sleep(1)

    for node in graph.nodes():
        if not visited[node]:
            dfs(node)

    return traversal_order

# Wczytanie grafu i wyświetlenie go
g = load_graph('data/graph.csv')
draw_graph(g, pos=nx.spring_layout(g), visited_nodes=set(), edge_colors='skyblue')

# Przeprowadzenie pełnego przeszukiwania grafu w głąb
dfs_order = traverse_full_dfs(g)
print("DFS Traversal Order:", dfs_order)
