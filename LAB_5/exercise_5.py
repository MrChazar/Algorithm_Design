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

n = [a for a in range(11)]
print(n)

# Stworzenie listy
lista = func.fill_list(n)
print(f"Lista {lista}")


# Zadanie 1
time_t_start = time_t.time()
print(f"Maksymalna: {ex1.maximal(lista)}")
time_t_end = time_t.time()
time_t_duration = time_t_end - time_t_start
print(f"Jej czas: {time_t_duration}")

time_t_start = time_t.time()
print(f"Druga maksymalna: {ex1.second_max(lista)}")
time_t_end = time_t.time()
time_t_duration = time_t_end - time_t_start
print(f"Jej czas: {time_t_duration}")

time_t_start = time_t.time()
print(f"Średnia: {ex1.mean(lista)}")
time_t_end = time_t.time()
time_t_duration = time_t_end - time_t_start
print(f"Jej czas: {time_t_duration}")

# Zadanie 2
matrix_1 = func.create_matrix(n)
matrix_2 = func.create_matrix(n)

time_t_start = time_t.time()
print(f"Mnożenie macierzy: {ex2.multiply_matrix(matrix_1, matrix_2)}")
time_t_end = time_t.time()
time_t_duration = time_t_end - time_t_start
print(f"Jej czas: {time_t_duration}")

# Zadanie 3
time_t_start = time_t.time()
print(f"Kombinacje: {ex3.every_combination(lista)}")
time_t_end = time_t.time()
time_t_duration = time_t_end - time_t_start
print(f"Jej czas: {time_t_duration}")
