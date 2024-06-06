"""
1 Zadanie nr 1 – sortowanie przez kopcowanie
Wykorzystaj dane (flota robotów) z poprzedniej listy.
Zaimplementuj algorytm sortowania przez kopcowanie względem ceny robota.
Zadanie uzupełnij o tryb przechodzenia przez proces sortowania "krok-po-kroku". W tym trybie wyświetlaj
kopiec w kolesta robotów (wczytywana z pliku).
Wyjście: pojnych iteracjach algorytmu.
Wejście: lisortowana lista robotów (zapisana do pliku i wyświetlona).
"""

import LAB_9.exercise_1 as rob
import random


def generate_robots(n):
    robots = []

    for a in range(n):
        params = []

        t = random.randint(0,3)
        type = ""
        if (t == 0):
            type = "AGV"
        elif (t == 1):
            type = "AFV"
        elif (t == 2):
            type = "ASV"
        elif (t == 3):
            type = "AUV"

        price = int(random.randint(0, 1000))

        ranged = random.randint(0, 100)

        camera = random.random()

        robots.append((type, price, ranged, camera))
    return robots


# Funkcje pomocnicze do sortowania przez kopcowanie
def heapify(arr, n, i, step_by_step=False):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[i][1] < arr[left][1]:
        largest = left

    if right < n and arr[largest][1] < arr[right][1]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        if step_by_step:
            print_heap(arr)
        heapify(arr, n, largest, step_by_step)


def heap_sort(arr, step_by_step=False):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i, step_by_step)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        if step_by_step:
            print_heap(arr)
        heapify(arr, i, 0, step_by_step)


def print_heap(arr):
    df = pd.DataFrame(arr, columns=['Type', 'Price', 'Range', 'Camera'])
    print(df)





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


stack = []
removed_stack = []

control = 'e'

while(control != 'q'):
    control = input("Możesz - wczytać roboty: l, wyświetlić roboty: p, sortować po cenie: f, wyjść: q "
                    "Wybór:")

    if control == 'r':
        remove_robot(stack, removed_stack)

    if control == 'l':
        stack += rob.generate_robots(100)

    if control == 'p':
        rob.show_robots(stack)

    if control == 'f':
        step_by_step = input("Czy chcesz tryb krok-po-kroku? (y/n): ").lower() == 'y'
        heap_sort(stack, step_by_step)
        rob.show_robots(stack)