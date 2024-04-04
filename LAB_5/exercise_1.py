"""
Zadanie nr 1
Dla listy liczb zadanej przez użytkownika, zaimplementuj algorytm (algorytmy)
1. znajdujący największy element na liście,
2. znajdujący drugi największy element na liście,
3. obliczający średnią elementów na liście.
"""

import functions as func


# Maksymalna liczba
# Złożoność algorytmiczna o(n)
def maximal(list):
    max = int(list[0])
    for a in range(1, len(list)):
        if int(list[a]) > max:
            max = list[a]
    return max


# Druga Maksymalna Liczba
# Złożoność obliczeniowa: O(n^2)
def second_max(list):
    max = maximal(list)
    new_max  = 0
    for a in range(len(list)):
        if list[a] == max:
            continue
        if int(list[a]) > new_max:
            new_max = list[a]
    return new_max


# Średnia elementów na liście
def mean(list):
    sum = 0
    for a in range(len(list)):
        sum += int(list[a])
    return sum / len(list)


"""
lista = func.fill_list(2)
print(lista)

print(f"Max: {maximal(lista)}")
print(f"Second Max: {second_max(lista)}")
print(f"Mean: {mean(lista)}")
"""

