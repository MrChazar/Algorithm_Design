"""
Napisz program symulujący działanie automatu skończonego opisanego jak następuje. Symulujący, czyli
pokazujący konfigurację automatu w kolejnych krokach. Umożliw podanie dowolnego wejścia (zgodnego z
alfabetem).
• Q = {q0, q1, q2, q3},
• Σ = {0, 1},
• δ :
0 1
q0 q1 q0
q1 q3 q2
q2 q2 q0
q3 q2 q2
,
• q0 to stan początkowy,
• F = {q3}.
"""

def ended_automaton(input, list_of_states, delta, initial_state, final_state):
    current_state = initial_state
    for a in input:
        print(f'Aktualny stan: {current_state}, wejście: {a}')
        current_state = delta[current_state][a]
    if current_state == final_state:
        print(f'Wejście {input} akceptowane')
        return True
    else:
        print(f'Wejście {input} odrzucone')
        return False

# Parametry wejściowe
list_of_states = ['q0', 'q1', 'q2', 'q3']
list_of_input = ['0', '1']
delta = {
    'q0': {'0': 'q1', '1': 'q0'},
    'q1': {'0': 'q3', '1': 'q2'},
    'q2': {'0': 'q2', '1': 'q0'},
    'q3': {'0': 'q2', '1': 'q2'}
}
initial_state = 'q0'
final_state = 'q3'
input = '101010'
current_state = initial_state

ended_automaton(input, list_of_states, delta, initial_state, final_state)