"""
Zadanie nr 5
Dla każdej wersji zadania nr 4, czyli dla problemów z zadań 1, 2 i 3 wykonaj:
• dla każdego n ∈ {1, 2, 3, . . . , 10} uruchom program po 10 razy,
• na wykresie od n (oś odciętych) wyświetl średni, minimalny i maksymalny czas działania algorytmu,
• przerwij działanie programu, jeśli wykonuje się dłużej niż 10 minut; ogranicz wykresy tylko do uzyskanych rezultatów,
• zestaw wykresy ze złożonością oszacowaną analitycznie.
Wyjście: 3 układy współrzędnych (dla problemów z zadań 1, 2, 3), każdy po 3 wykresy (średni, minimalny i
maksymalny czas działania).
"""
import functions as func
import exercise_1 as ex1
import exercise_2 as ex2
import exercise_3 as ex3
import time as time_t
import matplotlib.pyplot as plt
import numpy as np

n_values = list(range(1, 100 ))
num_trials = 10
max_execution_time = 600  # 10 minut w sekundach

# Zbieranie wyników czasu wykonania dla każdego zadania i wartości n
results = {
    'Maksimum': {'max': [], 'min': [], 'avg': []},
    'Mnożenie Macierzy': {'max': [], 'min': [], 'avg': []},
    'Kombinacje': {'max': [], 'min': [], 'avg': []}
}

for n in n_values:
    print(f"n = {n}")
    lista = func.fill_list(n)

    # Maksimum
    times_max = []
    for _ in range(num_trials):
        start_time = time_t.time()
        ex1.maximal(lista)
        end_time = time_t.time()
        execution_time = end_time - start_time
        times_max.append(execution_time)

    results['Maksimum']['max'].append(max(times_max))
    results['Maksimum']['min'].append(min(times_max))
    results['Maksimum']['avg'].append(sum(times_max) / num_trials)

    # Mnożenie Macierzy
    times_multiply = []
    for _ in range(num_trials):
        matrix_1 = func.create_matrix(n)
        matrix_2 = func.create_matrix(n)
        start_time = time_t.time()
        ex2.multiply_matrix(matrix_1, matrix_2)
        end_time = time_t.time()
        execution_time = end_time - start_time
        times_multiply.append(execution_time)

    results['Mnożenie Macierzy']['max'].append(max(times_multiply))
    results['Mnożenie Macierzy']['min'].append(min(times_multiply))
    results['Mnożenie Macierzy']['avg'].append(sum(times_multiply) / num_trials)

    # Kombinacje
    times_combinations = []
    for _ in range(num_trials):
        start_time = time_t.time()
        ex3.every_combination(lista)
        end_time = time_t.time()
        execution_time = end_time - start_time
        times_combinations.append(execution_time)

    results['Kombinacje']['max'].append(max(times_combinations))
    results['Kombinacje']['min'].append(min(times_combinations))
    results['Kombinacje']['avg'].append(sum(times_combinations) / num_trials)

# Narysowanie wykresów
fig, axs = plt.subplots(3, 3, figsize=(15, 10), sharex=True)

task_titles = ['Maksimum', 'Mnożenie Macierzy', 'Kombinacje']
metrics = ['max', 'min', 'avg']

for i, task_title in enumerate(task_titles):
    for j, metric in enumerate(metrics):
        ax = axs[i, j]
        ax.plot(n_values, results[task_title][metric], marker='o', linestyle='-', label=metric)
        ax.set_xlabel('n')
        ax.set_ylabel('Czas (s)')
        ax.set_title(f'{task_title} - {metric.capitalize()}')
        ax.grid(True)

fig.tight_layout()
plt.show()
