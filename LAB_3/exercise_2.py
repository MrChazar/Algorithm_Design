"""
Napisz program symulujący działanie maszyny Turinga o grafie przejść jak na Rys. 1 (zbiór stanów i alfabet
są takie, jakie wynikają z grafu). Symulujący, czyli pokazujący konfigurację maszyny w kolejnych krokach.
Umożliw podanie dowolnego wejścia (zgodnego z alfabetem).
Wejście: słowo na taśmie.
Wyjście: symulacja działania maszyny (w konsoli).
"""

def ended_automaton(input, delta, current_state, final_state):
    a = 0
    input = list(input)
    while True:
        print(f'Aktualny stan: {current_state[0]}, znak: {input[a]} indeks głowicy: {a} input: {input}')
        if input[a] not in list_of_input:
            print(f'Wejście {input} odrzucone - niepoprawne wejście')
        try:
            current_state = delta[current_state[0]][input[a]]
        except:
            print(f'Wejście {input} odrzucone - niepoprawne wejście')
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

# Parametry wejściowe
list_of_states = ['q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'qr', 'qa']
list_of_input = ['b', '0', '1', '␣']

delta = {
    'q0': {},
    'q0': {'a': ['q1', 'å', 'R'], '␣': ['qr', '', 'L']},
}

final_state = ['qr', 'qa']
input = 'aāa␣'
current_state = ['q0']


ended_automaton(input, delta, current_state, final_state)





