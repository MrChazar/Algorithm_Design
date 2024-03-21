"""
Przygotuj program, który zrealizuje algorytm sortowania przez wstawianie.
"""

import functions as func


def insertion_sort(n):
    for i in range(1, len(n)):
        key = n[i]
        j = i - 1
        while j >= 0 and key < n[j]:
            n[j + 1] = n[j]
            j -= 1
        n[j + 1] = key
    return n


tab = func.fill_list(10)
print(f"Lista: {tab}")
print(f"Posortowana {insertion_sort(tab)}")

