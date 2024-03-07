"""
Napisz program (niekoniecznie automat skończony) rozpoznający język A = {auaw : u, w ∈ {0, 1}∗}.
Wejście: ciąg wejściowy automatu.
Wyjście: informacja: język rozpoznany, język nierozpoznany
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

list_of_states = ['q0','q1','q2','q3']
list_of_input = ['0','1','a']

delta = {
    'q0': {'0': 'q1', '1': 'q0', 'a': 'q3'},
    'q1': {'0': 'q0', '1': 'q2', 'a': 'q0'},
    'q2': {'0': 'q2', '1': 'q0', 'a': 'q1'},
    'q3': {'0': 'q1', '1': 'q2', 'a': 'q0'}
}

initial_state = 'q0'
final_state = ['q2', 'q3']


input = 'a1001abad'

ended_automaton(input, delta, initial_state, final_state, list_of_input)