"""
Zadanie nr 1 – przeszukiwanie w głąb
Dla zadanego grafu wczytywanego z pliku zaimplementuj algorytm przeszukiwania w głąb.
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
    G = nx.from_pandas_adjacency(adj_matrix, create_using=nx.DiGraph)
    return G


def draw_graph(graph):
    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(graph)
    nx.draw(graph, pos, with_labels=True, node_size=700, node_color="skyblue", arrows=True)
    plt.show()


def traverse_dfs(graph, start_node):
    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(graph)
    visited = set()
    traversal_order = []

    def dfs(node):
        if node not in visited:
            visited.add(node)
            traversal_order.append(node)
            if visited:
                node_color = ['red' if node in visited else 'skyblue' for node in graph.nodes()]
            else:
                node_color = 'skyblue'
            nx.draw(graph, pos, with_labels=True, node_size=700, node_color=node_color, arrows=True)
            plt.show()
            time.sleep(1)
            for neighbor in graph.neighbors(node):
                dfs(neighbor)

    dfs(start_node)
    return traversal_order


def traverse_full_dfs(graph):
    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(graph)
    visited = set()
    traversal_order = []

    def dfs(node):
        if node not in visited:
            visited.add(node)
            traversal_order.append(node)
            if visited:
                node_color = ['red' if node in visited else 'skyblue' for node in graph.nodes()]
            else:
                node_color = 'skyblue'
            nx.draw(graph, pos, with_labels=True, node_size=700, node_color=node_color, arrows=True)
            plt.show()
            time.sleep(1)  # Opóźnienie dla lepszego efektu wizualnego
            for neighbor in graph.neighbors(node):
                dfs(neighbor)

    for node in graph.nodes():
        if node not in visited:
            dfs(node)
    return traversal_order


g = load_graph('data/graph.csv')
draw_graph(g)
traverse_dfs(graph=g, start_node=1)