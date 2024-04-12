"""
Dla listy liczb zadanej przez użytkownika, zaimplementuj algorytm (algorytmy) rekurencyjne
1. znajdujący największy element na liście,
2. znajdujący drugi największy element na liście,
3. obliczający średnią elementów na liście.
< --- >
Algorytmy dzielą listę na dwie (w przybliżeniu) połowy i uruchamiają się rekurencyjnie na utworzonych
połowach.
Wejście: lista liczb.
Wyjście: jak w 1, 2, 3.
Oszacuj złożoność czasową algorytmów.
"""

import random
import functions as func


def biggest_element(A, n):
    if (n == 1):
        return A[0]
    return max(A[n - 1], biggest_element(A, n - 1))


def  second_biggest_element(A, n):
    A.remove(biggest_element(A, n))
    return biggest_element(A, n-1)


def mean_element(A, N):
    if (N == 1):
        return A[N - 1]
    else:
        return ((mean_element(A, N - 1) * (N - 1) + A[N - 1]) / N)

lista = func.fill_list(10)

print(f"Lista: {lista}")
print(f"Największy element używając rekurencji: {biggest_element(lista, len(lista))}")
print(f"Największy drugi element używając rekurencji: {second_biggest_element(lista, len(lista))}")
print(f"Średni element używając rekurencji: {mean_element(lista, len(lista))}")