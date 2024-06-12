"""
Zadanie nr 3 – sortowanie przez zliczanie
Wykorzystaj dane (flota robotów) z poprzedniej listy.
Zaimplementuj algorytm sortowania przez zliczanie względem zasięgu robota.
Wejście: lista robotów (wczytywana z pliku).
Wyjście: posortowana lista robotów (zapisana do pliku i wyświetlona)
"""
import random
import pandas as pd
import LAB_9.exercise_1 as rob

# Funkcja do generowania robotów
def generate_robots(n):
    robots = []

    for a in range(n):
        t = random.randint(0, 3)
        type = ["AGV", "AFV", "ASV", "AUV"][t]
        price = int(random.randint(0, 1000))
        ranged = random.randint(0, 100)
        camera = random.random()

        robots.append((type, price, ranged, camera))
    return robots

# Funkcja pomocnicza do wyświetlania stanu listy robotów
def print_robots(arr):
    df = pd.DataFrame(arr, columns=['Type', 'Price', 'Range', 'Camera'])
    print(df)

# Implementacja sortowania przez zliczanie
def counting_sort(arr):
    max_range = max(arr, key=lambda x: x[2])[2]
    min_range = min(arr, key=lambda x: x[2])[2]
    range_count = max_range - min_range + 1

    count = [0] * range_count
    output = [None] * len(arr)

    for robot in arr:
        count[robot[2] - min_range] += 1

    for i in range(1, range_count):
        count[i] += count[i - 1]

    for robot in reversed(arr):
        output[count[robot[2] - min_range] - 1] = robot
        count[robot[2] - min_range] -= 1

    return output

def clear_robots(robots, removed_robots):
    while robots:
        a = robots.pop(0)
        removed_robots.append(a)
    print("Roboty usunięte razem z tymi z oczyszczenia")
    rob.show_robots(removed_robots)

# Główna pętla sterująca
stack = []
removed_stack = []

control = 'e'

while(control != 'q'):
    control = input("Możesz - wczytać roboty: l, wyświetlić roboty: p, sortować po zasięgu: f, wyjść: q\nWybór:")

    if control == 'l':
        stack += rob.generate_robots(100)

    if control == 'p':
        rob.show_robots(stack)

    if control == 'f':
        step_by_step = input("Czy chcesz tryb krok-po-kroku? (y/n): ").lower() == 'y'
        sorted_stack = counting_sort(stack)
        if step_by_step:
            print_robots(sorted_stack)
        rob.show_robots(sorted_stack)
        stack = sorted_stack

