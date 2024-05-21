"""
Porównaj prędkość działania algorytmów wyszukiwania zaimplementowanych w zadaniach 3 i 4.
1. W razie potrzeby, zmodyfikuj listę robotów tak, aby ich parametry CENA były unikatowe.
2. Posortuj listę robotów względem parametru CENA.
3. Wyszukuj po pojedynczej wartości parametru CENA.
4. Algorytmy wyszukiwania uruchamiaj dla kolejnych robotów, tzn. szukaj po cenach istniejących robotów
(czyli zawsze zostanie znaleziony dokładnie jeden robot).
5. Wyniki przedstaw na wykresie średniego czasu wyszukiwania robota (po wszystkich robotach).
6. Wynik przedstaw dla kilku wartości współczynnika α.
Wejście: lista robotów (wczytywana z pliku), współczynnik α.
Wyjście: wykresy średniego czasu wyszukiwania robota.
"""

import numpy as np
import random
import pandas as pd
import time
import matplotlib.pyplot as plt
import LAB_9.exercise_1 as rob  # Upewnij się, że LAB_9.exercise_1 jest poprawnie zaimportowane

# Funkcja haszująca
def hash_function(key, size):
    return hash(key) % size

# Modyfikacja listy robotów, aby ceny były unikatowe
def modify_robot_prices(robots):
    for i, robot in enumerate(robots):
        robots[i] = (robot[0], i + 1, robot[2], robot[3])  # Nadaj unikatowe ceny od 1 do n
    return robots

# Sortowanie listy robotów względem ceny
def sort_robots_by_price(robots):
    return sorted(robots, key=lambda x: x[1])

# Pomiar czasu wyszukiwania dla zadania 3
def measure_search_time_task3(robots, alpha):
    hash_table = create_hash_table_task3(robots, 1, alpha)
    search_times = []
    for robot in robots:
        start_time = time.time()
        search_in_hash_table_task3(hash_table, robot[1], 1)
        end_time = time.time()
        search_times.append(end_time - start_time)
    return np.mean(search_times)

# Pomiar czasu wyszukiwania dla zadania 4
def measure_search_time_task4(robots, alpha):
    hash_table = create_hash_table_task4(robots, 1, alpha)
    search_times = []
    for robot in robots:
        start_time = time.time()
        search_in_hash_table_task4(hash_table, robot[1], 1)
        end_time = time.time()
        search_times.append(end_time - start_time)
    return np.mean(search_times)

# Wykres średnich czasów wyszukiwania
def plot_search_times(search_times_task3, search_times_task4, alphas):
    plt.plot(alphas, search_times_task3, label='Algorytm z zadania 3')
    plt.plot(alphas, search_times_task4, label='Algorytm z zadania 4')
    plt.xlabel('Współczynnik α')
    plt.ylabel('Średni czas wyszukiwania (s)')
    plt.legend()
    plt.title('Porównanie średniego czasu wyszukiwania robotów')
    plt.show()

# Funkcje z zadania 3
def create_hash_table_task3(robots, param_index, alpha):
    table_size = int(len(robots) / alpha)
    hash_table = [None] * table_size
    for robot in robots:
        insert_robot_task3(hash_table, robot, param_index)
    return hash_table

def insert_robot_task3(table, robot, param_index):
    key = robot[param_index]
    index = hash_function(key, len(table))
    if table[index] is None:
        table[index] = []
    table[index].append(robot)

def search_in_hash_table_task3(table, key, param_index):
    index = hash_function(key, len(table))
    if table[index] is not None:
        for robot in table[index]:
            if robot[param_index] == key:
                return robot
    return "brak"

# Funkcje z zadania 4
def create_hash_table_task4(robots, param_index, alpha):
    table_size = int(len(robots) / alpha)
    hash_table = [None] * table_size
    for robot in robots:
        insert_robot_task4(hash_table, robot, param_index)
    return hash_table

def insert_robot_task4(table, robot, param_index):
    key = robot[param_index]
    index = hash_function(key, len(table))
    i = 0
    while table[index] is not None:
        i += 1
        index = (index + i**2) % len(table)
    table[index] = robot

def search_in_hash_table_task4(table, key, param_index):
    index = hash_function(key, len(table))
    i = 0
    while table[index] is not None and i < len(table):
        if table[index][param_index] == key:
            return table[index]
        i += 1
        index = (index + i**2) % len(table)
    return "brak"

# Główna funkcja wykonawcza
def main():
    robots = rob.read_robots()  # Wczytaj roboty z pliku
    robots = modify_robot_prices(robots)  # Modyfikuj ceny
    robots = sort_robots_by_price(robots)  # Sortuj względem ceny

    alphas = [0.1, 0.2, 0.3, 0.4, 0.5]  # Różne wartości współczynnika α
    search_times_task3 = []
    search_times_task4 = []

    for alpha in alphas:
        search_times_task3.append(measure_search_time_task3(robots, alpha))
        search_times_task4.append(measure_search_time_task4(robots, alpha))

    plot_search_times(search_times_task3, search_times_task4, alphas)

if __name__ == "__main__":
    main()


