"""
Napisz program (niekoniecznie maszynę Turinga), który rozstrzyga A = {axb : a, b ∈ (Σ − {x})∗, |a| = |b|}.
Wejście: alfabet wejściowy Σ, słowo (na taśmie).
Wyjście: informacja: język rozstrzygnięty, język nierozstrzygnięty.
"""

def turing_machine(input, delta, list_of_input, current_state, final_state, reject_state):
    a = 0
    input = list(input)
    while True:
        print(f'Aktualny stan: {current_state[0]}, znak: {input[a]} indeks głowicy: {a} input: {input}')
        if input[a] not in list_of_input:
            print(f'Wejście {input} odrzucone - niepoprawne wejście')
        try:
            current_state = delta[current_state[0]][input[a]]
        except:
            print(f'Wejście {input} odrzucone - brak możliwości przejścia dalej')
            return False

        if current_state[1] != '':
            input[a] = current_state[1]
        if current_state[2] == 'R':
            a += 1
            if a > len(input)-1:
                a = 0
        elif current_state[2] == 'L':
            a -= 1
            if a < 0:
                a = 0
        print(f'Stan po wejściu: {current_state[0]}')
        if current_state[0] in final_state:
            print(f'Wejście {input} akceptowane')
            return True
        elif current_state[0] in reject_state:
            print(f'Wejście {input} odrzucone')
            return False


# Parametry wejściowe
list_of_states = ['q0', 'q1', 'q2', 'qa', 'qr']
list_of_input = ['a', 'b', 'x', '␣']
delta = {
    'q0': {'a': ['q1', 'b', 'R'], 'b': ['q0', '␣', 'L'], 'x': ['qr', '␣', 'R']},
    'q1': {'a': ['q2', '␣', 'R'], 'b': ['q1', '␣', 'L'], 'x': ['qr', '␣', 'R']},
    'q2': {'a': ['qa', '␣', 'R'], 'b': ['qa', '␣', 'R'], 'x': ['q1', '␣', 'L']}
}


final_state = ['qa']
reject_state = ['qr']

input = 'aabxa'
current_state = ['q0']

# Test programu
turing_machine(input, delta, list_of_input, current_state, final_state, reject_state)