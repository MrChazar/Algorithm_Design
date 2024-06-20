"""
Zadanie nr 4 – sortowanie topologiczne
Dla zadanego grafu wczytywanego z pliku zaimplementuj algorytm sortowania topologicznego z wykorzystaniem DFS
Procedurę przedstaw graficznie, krok po kroku.
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


def draw_graph(graph, pos, visited, stack):
    plt.figure(figsize=(8, 6))
    node_color = ['red' if node in visited else 'skyblue' for node in graph.nodes()]
    edge_color = ['green' if edge in stack else 'black' for edge in graph.edges()]
    nx.draw(graph, pos, with_labels=True, node_size=700, node_color=node_color, edge_color=edge_color, arrows=True)
    plt.show()

def topological_sort_dfs(graph):
    pos = nx.spring_layout(graph)
    visited = set()
    stack = []
    traversal_order = []

    def dfs(node):
        visited.add(node)
        traversal_order.append(node)
        draw_graph(graph, pos, visited, stack)
        time.sleep(1)

        for neighbor in graph.neighbors(node):
            if neighbor not in visited:
                dfs(neighbor)

        stack.append(node)

    for node in graph.nodes():
        if node not in visited:
            dfs(node)

    stack.reverse()
    return stack


g = load_graph('data/graph.csv')
draw_graph(g, pos=nx.spring_layout(g), visited=set(), stack=[])


topological_order = topological_sort_dfs(g)
print("Topological Sort Order:", topological_order)
