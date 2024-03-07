"""
Napisz program symulujący automat rozpoznający język B = {anbcdm : n ≥ 0, m ≥ 0}. Przedstaw symulację
dla zadanego ciągu wejściowego.
Wejście: ciąg wejściowy automatu.
Wyjście: symulacja działania automatu (w konsoli).
"""

def ended_automaton(input, delta, initial_state, final_state, list_of_input):
    current_state = initial_state
    for a in input:
        if a not in list_of_input:
            print(f'Wejście {input} odrzucone - niepoprawne wejście')
            return False
        print(f'Aktualny stan: {current_state}, wejście: {a}')
        current_state = delta[current_state][a]
    if current_state in final_state:
        print(f'Wejście {input} akceptowane')
        return True
    else:
        print(f'Wejście {input} odrzucone')
        return False

list_of_states = ['q0','q1','q2','q3','q4']
list_of_inputs = ['a','b','c','d']
delta = {
    'q0': {'a': 'q1', 'b': 'q4', 'c': 'q4', 'd': 'q4'},
    'q1': {'a': 'q1', 'b': 'q2', 'c': 'q4', 'd': 'q4'},
    'q2': {'a': 'q3', 'b': 'q4', 'c': 'q4', 'd': 'q4'},
    'q3': {'a': 'q3', 'b': 'q4', 'c': 'q2', 'd': 'q4'},
    'q4': {'a': 'q4', 'b': 'q4', 'c': 'q4', 'd': 'q4'}
}

initial_state = 'q0'
final_state = ['q2','q4']

input = 'ab1232acada'
ended_automaton(input, delta, initial_state, final_state, list_of_inputs)
