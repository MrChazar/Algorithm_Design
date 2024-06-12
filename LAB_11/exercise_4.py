"""
Zadanie nr 4 – sortowanie pozycyjne
Dana jest macierz (dwuwymiarowa tablica) M × N liczb całkowitych. Zaimplementuj algorytm sortowania
pozycyjnego wierszy tablicy.
Sortowanie wykonuj tak, aby o kolejności najpierw decydowała pierwsza kolumna. W przypadku, gdy wartości
w pierwszej kolumnie są jednakowe, o kolejności decyduje druga kolumna. W przypadku, gdy wartości w
drugiej kolumnie też są jednakowe, o kolejności decyduje trzecia kolumna, itd.
Wejście: zadana przez użytkownika macierz liczb całkowitych.
Wyjście: posortowana macierz liczb całkowitych.
"""

import random
import pandas as pd


# Funkcja do generowania macierzy
def generate_matrix(m, n):
    return [[random.randint(0, 100) for _ in range(n)] for _ in range(m)]


# Funkcja pomocnicza do wyświetlania stanu macierzy
def print_matrix(matrix):
    df = pd.DataFrame(matrix)
    print(df)


# Implementacja sortowania pozycyjnego dla wierszy macierzy
def radix_sort_matrix(matrix):
    if not matrix:
        return matrix

    num_columns = len(matrix[0])

    for col in range(num_columns - 1, -1, -1):
        matrix.sort(key=lambda x: x[col])

    return matrix


# Główna pętla sterująca
matrix = []

control = 'e'

while (control != 'q'):
    control = input("Możesz - wczytać macierz: l, wyświetlić macierz: p, sortować: s, wyjść: q\nWybór:")

    if control == 'l':
        m = int(input("Podaj liczbę wierszy: "))
        n = int(input("Podaj liczbę kolumn: "))
        matrix = generate_matrix(m, n)
        print_matrix(matrix)

    if control == 'p':
        print_matrix(matrix)

    if control == 's':
        step_by_step = input("Czy chcesz tryb krok-po-kroku? (y/n): ").lower() == 'y'
        if step_by_step:
            for col in range(len(matrix[0]) - 1, -1, -1):
                matrix.sort(key=lambda x: x[col])
                print(f"Sortowanie według kolumny {col + 1}:")
                print_matrix(matrix)
        else:
            matrix = radix_sort_matrix(matrix)
        print("Posortowana macierz:")
        print_matrix(matrix)

