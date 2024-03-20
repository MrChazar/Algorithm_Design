import re
"""
Niech na wejściu maszyny Turinga będzie ciąg reprezentujący listę wierzchołków zadanego grafu < G > .
Każdy wierzchołek jest reprezentowany przez dowolne słowo generowane alfabetem {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}.
Wierzchołki []
Zaproponuj (pseudokod) maszynę Turinga weryfikującą, czy układ nawiasów, przecinków i cyfr jest poprawny.
Oszacuj złożoność czasową maszyny.
Wyjście: maszyna Turinga, oszacowanie złożoności
"""

"""
Mój pseudokod bardziej pseudo niż kod którego złożoność wynosi O(n), gdzie n to długość wejścia.
1. Jeśli pierwszy symbol to '[', przejdź do kroku 2, w przeciwnym razie zwróć fałsz.
2. Inicjuj listę unikalnych liczb.
3. Dla każdego elementu w sekwencji:
    a. Jeśli element jest liczbą, sprawdź czy nie znajduje się już w liście unikalnych liczb. Jeśli nie, dodaj do listy.
    b. Jeśli element to kropki, sprawdź czy są dokładnie 3. Jeśli tak, przejdź do kroku 4, w przeciwnym razie zwróć fałsz.
    c. Jeśli element to przecinek, przejdź do kroku 5.
4. Sprawdź czy kolejny element to liczba zakończona przecinkiem. Jeśli tak, dodaj do listy unikalnych liczb i przejdź do kroku 3, w przeciwnym razie zwróć fałsz.
5. Sprawdź czy sekwencja kończy się na '...]' i zakończ operację zwracając prawdę, w przeciwnym razie zwróć fałsz.

"""

def turing_machine(input, delta, list_of_input, current_state, final_state, reject_state):
    a = 0
    if not check_input(input):
        print(f'Wejście {input} odrzucone - niepoprawne wejście')
        return False
    input = turn_to_n(input)
    print(input)
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


def check_input(input):
    input = input.replace('[', '.').replace(']', '.').replace(',', '.').replace('␣', '.')
    input = input.split('.')
    numbers = []
    print(input)
    for a in input:
        if a == '':
            continue
        if a.isdigit() == False:
            return False
        if int(a[0]) == 0:
            return False
        if int(a) not in numbers:
            numbers.append(int(a))
        else:
            return False
    return True

def turn_to_n(input):
    def replace_numbers(match):
        return 'nn'
    output_string = re.sub(r'\d+', replace_numbers, input)
    return output_string


# Parametry wejściowe
list_of_states = ['q0', 'qr', 'qa', 'q3', 'q4', 'q1', 'q2']
list_of_input = ['n', ',', '.', '[', ']', '␣', 'n'] # gdzie n należy do {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
delta = {
    'q0': {'␣': ['qr', '', 'L'], '[': ['q1', '', 'R'], 'n': ['qr', '', 'R']},
    'q1': {'n': ['q1', '', 'R'], '[': ['qr', '', 'R'], ']': ['qr', '', 'R'], '.': ['q3', '', 'R'], ',': ['q1', '', 'R']},
    'q3': {'.': ['q3', '', 'R'], ']': ['q4', '', 'R'], ',': ['q2', '', 'R']},
    'q4': {'␣': ['qa', '', 'L'], ']': ['qr', '', 'R'], 'n': ['qr', '', 'R'], ',': ['qr', '', 'R']},
    'q2': {'n': ['q1', '', 'R'], ',': ['qr', '', 'R']}
}


final_state = ['qa']
reject_state = ['qr']


input = '[21...,23,...,12,...,32,...,13,...]␣'
print(check_input(input))


print(len(input))
current_state = ['q0']


# Test programu
turing_machine(input, delta, list_of_input, current_state, final_state, reject_state)