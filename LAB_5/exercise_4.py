"""
 Zadanie nr 4
Dla programów napisanych w zadaniu nr 1 niech n będzie długością listy. Wykonaj czynności (napisz program):
1. dla n zadanego przez użytkownika wygeneruj (losowo) listę liczb (skorzystaj z wbudowanego generatora
liczb losowych),
2. uruchom program z zadania nr 1 na wygenerowanej liście,
3. zwróć czas działania programu (z zadania nr 1, nie samej generacji listy) dla zadanego n.
Powtórz czynności dla zadania nr 2 przyjmując za n rozmiar macierzy. Macierze generuj losowo.
Powtórz czynności dla zadania nr 3 przyjmując za n długość listy. Listę generuj losowo.
Wejście: n, wersja programu (z zadania nr 1, 2 lub 3 – może być w osobnych programach).
Wyjście: czas działania programu.
"""

import functions as func
import exercise_1 as ex1
import exercise_2 as ex2
import  exercise_3 as ex3
import time as time_t

n = 100000

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
