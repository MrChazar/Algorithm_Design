"""
Napisz program symulujący działanie maszyny Turinga o grafie przejść jak na Rys. 1 (zbiór stanów i alfabet
są takie, jakie wynikają z grafu). Symulujący, czyli pokazujący konfigurację maszyny w kolejnych krokach.
Umożliw podanie dowolnego wejścia (zgodnego z alfabetem).
Wejście: słowo na taśmie.
Wyjście: symulacja działania maszyny (w konsoli).
"""

def turing_machine(input, delta, current_state, final_state, reject_state):
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
        elif current_state[0] in reject_state:
            print(f'Wejście {input} odrzucone')
            return False

# Parametry wejściowe
list_of_states = ['q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'qr', 'qa']
list_of_input = ['0/', '1/', 'b', '␣', '0', '1']

delta = {
    'q0': {'b': ['q1', '', 'R'], '0': ['q2', '0/', 'R'], '1': ['q3', '1/', 'R']},
    'q1': {'0/': ['q1', '', 'R'], '1/': ['q1', '', 'R'], '␣': ['qa', '', 'L'], '1': ['qr', '', 'L'], '0': ['qr', '', 'L']},
    'q2': {'␣': ['qr', '', 'R'], 'b': ['q4', '', 'R'], '0': ['q2', '', 'R'], '1': ['q2', '', 'R']},
    'q3': {'␣': ['qr', '', 'R'], 'b': ['q5', '', 'R'], '0': ['q3', '', 'R'], '1': ['q3', '', 'R']},
    'q4': {'0/': ['q4', '', 'R'], '1/': ['q4', '', 'R'], '␣': ['qr', '', 'R'], '1': ['qr', '', 'R'], '0': ['q6', '0/', 'L']},
    'q5': {'0/': ['q5', '', 'R'], '1/': ['q5', '', 'R'], '␣': ['qr', '', 'R'], '0': ['qr', '', 'R'], '1': ['q6', '1/', 'L']},
    'q6': {'b': ['q7', '', 'L'], '0/': ['q6', '', 'L'], '1/': ['q6', '', 'L']},
    'q7': {'0': ['q7', '', 'L'], '1': ['q7', '', 'L'], '0/': ['q0', '', 'R'], '1/': ['q0', '', 'R']}
}

final_state = ['qa']
reject_state = ['qr']
input = 'b␣'
current_state = ['q0']

turing_machine(input, delta, current_state, final_state, reject_state)





