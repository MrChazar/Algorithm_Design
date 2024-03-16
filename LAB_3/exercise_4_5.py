"""
Niech na wejściu maszyny Turinga będzie ciąg reprezentujący listę wierzchołków zadanego grafu < G > .
Każdy wierzchołek jest reprezentowany przez dowolne słowo generowane alfabetem {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}.
Wierzchołki []
Zaproponuj (pseudokod) maszynę Turinga weryfikującą, czy układ nawiasów, przecinków i cyfr jest poprawny.
Oszacuj złożoność czasową maszyny.
Wyjście: maszyna Turinga, oszacowanie złożoności
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
list_of_states = ['q0', 'qr', 'qa', ]
list_of_input = ['n', ',', '.', '[', ']', '␣', 'n'] # gdzie n należy do {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
delta = {
    'q0': {'␣': ['qr', '', 'L'], '[': ['q1', '', 'R'], 'n': ['qr', '', 'R']},
    'q1': {'n': ['q1', '', 'R'], '[': ['qr', '', 'R'], ']': ['qr', '', 'R'], '.': ['q3', '', 'R']},
    'q3': {'.': ['q3', '', 'R'], ']': ['q4', '', 'R'], ',': ['q2', '', 'R']},
    'q4': {'␣': ['qa', '', 'L'], ']': ['qr', '', 'R'], 'n': ['qr', '', 'R'], ',': ['qr', '', 'R']},
    'q2': {'n': ['q1', '', 'R'], ',': ['qr', '', 'R']}
}


final_state = ['qa']
reject_state = ['qr']

input = '[nn...,nn,...,nn...]␣'
print(len(input))
current_state = ['q0']

# Test programu
turing_machine(input, delta, list_of_input, current_state, final_state, reject_state)