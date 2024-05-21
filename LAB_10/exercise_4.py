""" Zadanie nr 4 – adresowanie otwarte
Zaimplementuj kolejny algorytm wyszukiwania robota na liście.
1. Pobierz od użytkownika docelowy współczynnik wypełnienia tablicy α. Utwórz pustą tablicę o odpowiednim rozmiarze.
2. Zastosuj adresowanie otwarte kwadratowe do wypełnienia tablicy. Samodzielnie zaproponuj składowe
funkcje haszujące i inne parametry haszowania.
3. Zaimplementuj algorytm wyszukujący robota po zadanym parametrze i zadanej jego pojedynczej wartości. Algorytm zwraca pierwszego znalezionego robota lub „brak”, jeśli robota nie znajdzie.
Wejście: lista robotów (wczytywana z pliku), wybrany parametr szukanego robota i wartość parametru.
Wyjście: lista parametrów znalezionego robota lub „brak”.
"""
import LAB_9.exercise_1 as rob

def remove_robot(robots, removed_robots):
    removed = robots.pop(0)
    removed_robots.append(removed)
    print(f"Robot o parametrach: {removed} usunięty")

def clear_robots(robots, removed_robots):
    while robots:
        a = robots.pop(0)
        removed_robots.append(a)
    print("Roboty usunięte razem z tymi z oczyszczenia")
    rob.show_robots(removed_robots)

def hash_function(key, size):
    return hash(key) % size

def quadratic_probing(hash_table, key, size):
    index = hash_function(key, size)
    i = 0
    while hash_table[index] is not None and i < size:
        i += 1
        index = (index + i**2) % size
    return index

def insert_robot(table, robot, param_index):
    key = robot[param_index]
    index = hash_function(key, len(table))
    i = 0
    while table[index] is not None:
        i += 1
        index = (index + i**2) % len(table)
    table[index] = robot

def create_hash_table(robots, param_index, alpha):
    table_size = int(len(robots) / alpha)
    hash_table = [None] * table_size
    for robot in robots:
        insert_robot(hash_table, robot, param_index)
    return hash_table

def search_in_hash_table(table, key, param_index):
    index = hash_function(key, len(table))
    i = 0
    while table[index] is not None and i < len(table):
        if table[index][param_index] == key:
            return table[index]
        i += 1
        index = (index + i**2) % len(table)
    return "brak"

def search_robot(parameter, value):
    param_map = {'Type': 0, 'Price': 1, 'Range': 2, 'Camera': 3}
    param_index = param_map[parameter]

    if parameter != 'Type':
        value = float(value)

    alpha = float(input("Podaj docelowy współczynnik wypełnienia tablicy α: "))
    hash_table = create_hash_table(stack, param_index, alpha)

    return search_in_hash_table(hash_table, value, param_index)

stack = []
removed_stack = []

control = 'e'

while(control != 'q'):
    control = input("Możesz - dodać robota : a, usunąć robota: r, wczytać roboty: l, wyświetlić roboty: p, wyszukać robota: f , wyjść: q "
                    "Wybór:")
    if control == 'a':
        robot = rob.generate_robots(1)
        print(robot)
        stack.append(rob.add_robot(robot[0]))

    if control == 'r':
        remove_robot(stack, removed_stack)

    if control == 'l':
        stack += rob.read_robots()

    if control == 'p':
        rob.show_robots(stack)

    if control == 'f':
        parameter = input("Wybierz parametr: 'Type', 'Price', 'Range', 'Camera':")
        value = input("Wartość parametru:")
        print(search_robot(parameter, value))
