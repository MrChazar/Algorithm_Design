"""
5 Zadanie nr 5
Pobierz od użytkownika graf nieskierowany (dowolna struktura, może być z pliku). Wykorzystaj zbiory
rozłączne do weryfikacji czy dwa wierzchołki zadanego grafu należą do jednej spójnej składowej.
Wyświetl listy wierzchołków tworzących spójne składowe.
Wejście: Graf nieskierowany.
Wyjście: listy wierzchołków tworzących spójne składowe.
"""

import networkx as nx
import matplotlib.pyplot as plt

def create_graph():
    G = nx.Graph()
    # Pętla umożliwiająca użytkownikowi dodawanie krawędzi
    while True:
        node1 = input("Podaj pierwszy wierzchołek krawędzi (lub 'q' aby zakończyć): ")
        if node1 == 'q':
            break
        node2 = input("Podaj drugi wierzchołek krawędzi: ")
        weight = int(input("Podaj wagę krawędzi: "))
        G.add_edge(node1, node2, weight=weight)
    return G

def show_graph(G):
    pos = nx.spring_layout(G)
    labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_nodes(G, pos, node_size=500)
    nx.draw_networkx_labels(G, pos)
    nx.draw_networkx_edges(G, pos)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.show()

def find_connected_components(G):
    connected_components = []
    visited = set()

    for node in G.nodes:
        if node not in visited:
            connected_component = set()
            queue = [node]
            while queue:
                current_node = queue.pop(0)
                if current_node not in visited:
                    visited.add(current_node)
                    connected_component.add(current_node)
                    queue.extend(G.neighbors(current_node))
            connected_components.append(connected_component)

    return connected_components

def main():
    G = create_graph()
    show_graph(G)

    connected_components = find_connected_components(G)

    print("Wierzchołki tworzące spójne składowe:")
    for i, component in enumerate(connected_components, 1):
        print(f"Spójna składowa {i}: {component}")


if __name__ == "__main__":
    main()
