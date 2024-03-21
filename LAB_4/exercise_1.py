"""
Zadanie 1
Przygotuj rozwiązanie zawierające następującą funkcjonalność:
a) wypełnianie listy wartościami losowymi,
b) wyszukującą taki element zbioru, dla którego suma elementów wcześniejszych jest równa sumie
elementów następnych,
c) sprawdzający czy podana wartość znajduje się w tablicy, jeżeli tak to zwraca indeks tego elementu, w przeciwnym wypadku -1.
"""

import functions as func

# Złożoność obliczeniowa: O(n)
def find_element(arr, tab):
    for i in range(len(arr)):
        if arr[i] == tab:
            return i
    return -1

# Złożoność obliczeniowa: O(n^2)
def sum_of_previous_elements(arr):
    for i in range(len(arr)):
        if sum(arr[:i]) == sum(arr[i+1:]):
            print(f"Sum of previous elements: {sum(arr[:i])}, Sum of next elements: {sum(arr[i+1:])}")
            return arr[i]
    return -1

# a) wypełnianie listy wartościami losowymi
n = 10
arr = func.fill_list(n)
print(arr)

# c) sprawdzający czy podana wartość znajduje się w tablicy, jeżeli tak to zwraca indeks tego elementu, w przeciwnym wypadku -1.
tab = 5
print(find_element(arr, tab))

# b) wyszukującą taki element zbioru, dla którego suma elementów wcześniejszych jest równa sumie elementów następnych,
print(sum_of_previous_elements(arr))


