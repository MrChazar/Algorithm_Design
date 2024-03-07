import networkx as nx
import matplotlib.pyplot as plt
"""
Napisz program symulujący dowolny automat skończony zadany przez użytkownika (w pliku; zaproponuj
format pliku). Ogranicz się do alfabetów złożonych z dowolnego podzbioru abecadła (pomijając litery diakrytyzowane). Symuluj działanie automatu krok po kroku.
Wejście: automat skończony w zadanym formacie, ciąg wejściowy automatu.
Wyjście: symulacja działania automatu.
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

def write_automaton(list_of_states, list_of_inputs, delta, initial_state, final_state, file_name):
    with open(file_name, 'w') as file:
        for a in list_of_states:
            file.write(f'{a} ')
        file.write('\n')
        for a in list_of_inputs:
            file.write(f'{a} ')
        file.write('\n')
        file.write(f'{initial_state}')
        file.write('\n')
        for a in final_state:
            file.write(f'{a} ')
        file.write('\n')
        for a in delta:
            for b in delta[a]:
                file.write(f'{a} {b} {delta[a][b]}\n')

def read_automaton(file_name):
    list_of_states = []
    list_of_input = []
    initial_state = ''
    final_state = []
    delta = {}
    # Otwarcie pliku i przypisanie wartości do zmiennych
    with open(file_name, 'r') as file:
        # Odczytanie i przypisanie pierwszych czterech linii do odpowiednich zmiennych
        list_of_states = file.readline().strip().split()
        list_of_input = file.readline().strip().split()
        initial_state = file.readline().strip()
        final_state = file.readline().strip()

        # Odczytanie reszty linii i przypisanie ich do zmiennej delta
        for line in file:
            state, symbol, next_state = line.strip().split()
            if state not in delta:
                delta[state] = {}
            delta[state][symbol] = next_state

    return list_of_states, list_of_input, delta, initial_state, final_state

list_of_states, list_of_inputs, delta, initial_state, final_state = read_automaton('automaton_4.txt')
write_automaton(list_of_states, list_of_inputs, delta, initial_state, final_state, file_name='automaton_4.txt')
ended_automaton('abca', delta, initial_state, final_state.split(), list_of_inputs)