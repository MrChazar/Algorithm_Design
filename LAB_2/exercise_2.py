"""
Napisz program symulujący działanie automatu skończonego o grafie przejść jak na Rys. 1 (zbiór stanów i
alfabet są takie, jakie wynikają z grafu). Symulację dla zadanego ciągu wejściowego przedstaw na rozrysowanym grafie.
Wejście: ciąg wejściowy automatu.
Wyjście: symulacja działania automatu (graficznie)
"""

import networkx as nx
import matplotlib.pyplot as plt

# Parametry wejściowe
list_of_states = ['q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6']
list_of_input = ['a', 'b', 'c']
delta = {
    'q0': {'a': 'q2', 'b': 'q2', 'c': 'q2'},
    'q1': {'b': 'q0', 'a': 'q4', 'c': 'q3'},
    'q4': {'a': 'q0', 'b': 'q5', 'c': 'q5'},
    'q5': {'a': 'q4', 'b': 'q4', 'c': 'q4'},
    'q2': {'a': 'q1', 'b': 'q1', 'c': 'q6'},
    'q3': {'a': 'q3', 'b': 'q3', 'c': 'q3'},
    'q6': {'a': 'q3', 'b': 'q3', 'c': 'q3'}
}

initial_state = 'q0'
final_state = ['q0', 'q4', 'q5']

input = 'aabb'
current_state = initial_state

G = nx.DiGraph()
G.add_nodes_from(list_of_states)

edge_labels = {}

for a in input:
    next_state = delta[current_state][a]
    if (current_state, next_state) in edge_labels:
        edge_labels[(current_state, next_state)] += ', ' + a
    else:
        edge_labels[(current_state, next_state)] = a
    G.add_edge(current_state, next_state)
    current_state = next_state

for node in list_of_states:
    if not any([node in edge for edge in G.edges]):
        G.remove_node(node)

pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, arrows=True, arrowstyle='->')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.show()