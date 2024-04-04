"""
Zadanie nr 3
Dany jest zbiór liczb całkowitych A zadanych przez użytkownika. Zweryfikuj (testując wszystkie możliwe
kombinacje) czy dla jakiegokolwiek podzbioru zbioru A suma liczb jest równa dokładnie 0.
Wejście: zbiór liczb całkowitych
Wyjście: odpowiedź, czy istnieją szukane podzbiory; jeśli tak - wyświetl je.
Oszacuj złożoność czasową algorytmu.
"""
import functions as func


def sum_list(list):
    sum = 0
    for a in range(list):
        sum += list[a]
    return sum


# Złożoność obliczeniowa O(2**n)
def every_combination(lst):
    number_of_combinations = 2 ** len(lst)
    for i in range(number_of_combinations):
        subset = []
        for j in range(len(lst)):
            #print(f"Operacja Bitowa:{(i >> j) & 1}")
            if (i >> j) & 1:
                subset.append(lst[j])
        #print(subset)
        if sum(subset) == 0 and subset != []:
            #print(f"Dla listy: {subset}")
            return True
    return False


"""
lista = func.fill_list(10)
print(f"Lista: {lista}")
print(f"Kombinacje {every_combination(lista)}")
"""
