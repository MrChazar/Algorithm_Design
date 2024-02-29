import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
"""
Zmodyfikuj poprzedni program tak, aby wierzchołki stały się środkiem kół o jednakowym promieniu (zadanym przez użytkownika). Wierzchołki dodawaj do okręgu pojedynczo, w następujący sposób.
1. Losuj pozycję (x, y) nowego wierzchołka.
2. Wyświetl wierzchołek (dodaj do wyświetlanego grafu odpowiednie koło).
3. Sprawdź, czy koło o środku (x, y) zachodzi na dowolne inne koło.
4. Jeśli zachodzi, to: odrzuć wierzchołek, usuń wyświetlone wcześniej koło (możesz przerysować cały graf)
i wróć do 1. Przerwij procedurę dodawania wierzchołków, jeśli nie udało się dodać nowego w ciągu 10
iteracji.
Wejście: liczba wierzchołków, przedział na osi Ox, przedział na osi Oy, promień koła.
Wyjście: graf wyświetlany wierzchołek po wierzchołku (np. kolejny wierzchołek po naciśnięciu spacji).
"""

# Ustawianie Parametrów
number_of_vertices = 10
x_distribution = (0, 1)
y_distribution = (0, 1)
radius = 0.01

# Tworzenie grafu
g = nx.Graph()
pos = {}

def is_collision(pos, new_pos, radius):
    for p in pos.values():
        if np.linalg.norm(np.array(p) - np.array(new_pos)) < 2* radius:  # Sprawdź kolizję
            return True
    return False

def draw_graph(g, pos):
    plt.clf()  # Wyczyść rysunek
    nx.draw(g, pos, with_labels=True, node_color='skyblue', node_size=500, font_size=12)
    plt.pause(1)  # Pauza, aby zobaczyć aktualizację grafu

# Dodawanie wierzchołków
for i in range(number_of_vertices):
    attempt = 0
    while attempt < 10:  # Maksymalnie 10 prób dodania wierzchołka
        new_pos = (np.random.uniform(x_distribution[0], x_distribution[1]), np.random.uniform(y_distribution[0], y_distribution[1]))
        if not is_collision(pos, new_pos, radius):
            g.add_node(i)
            pos[i] = new_pos
            draw_graph(g, pos)
            break
        attempt += 1
plt.show()


