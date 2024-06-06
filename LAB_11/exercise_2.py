"""
2 Zadanie nr 2 – sortowanie szybkie
Wykorzystaj dane (flota robotów) z poprzedniej listy.
Zaimplementuj algorytm sortowania szybkiego względem ceny robota.
Zadanie uzupełnij o tryb przechodzenia przez proces sortowania "krok-po-kroku". W tym trybie wyświetlaj
listę cen w kolejnych wywołaniach rekurencyjnych algorytmu.
Wejście: lista robotów (wczytywana z pliku).
Wyjście: posortowana lista robotów (zapisana do pliku i wyświetlona).
"""
import random
import pandas as pd
import LAB_9.exercise_1 as rob  # Upewnij się, że LAB_9.exercise_1 jest poprawnie zaimportowane

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


# Implementacja sortowania szybkiego (quicksort) z trybem krok-po-kroku
def quicksort(arr, low, high, step_by_step=False):
    if low < high:
        pi = partition(arr, low, high, step_by_step)
        quicksort(arr, low, pi - 1, step_by_step)
        quicksort(arr, pi + 1, high, step_by_step)


def partition(arr, low, high, step_by_step=False):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j][1] <= pivot[1]:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            if step_by_step:
                print_robots(arr)

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    if step_by_step:
        print_robots(arr)
    return i + 1


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
    control = input("Możesz - wczytać roboty: l, wyświetlić roboty: p, sortować po cenie: f, wyjść: q\nWybór:")

    if control == 'l':
        stack += rob.generate_robots(100)

    if control == 'p':
        rob.show_robots(stack)

    if control == 'f':
        step_by_step = input("Czy chcesz tryb krok-po-kroku? (y/n): ").lower() == 'y'
        quicksort(stack, 0, len(stack) - 1, step_by_step)
        rob.show_robots(stack)


