"""
Napisz program zawierający realizujący funkcję sortowania danych metodą przez scalanie
"""

import functions as func

def merge_sort(arr):
    n = len(arr)
    if n > 1:
        sub_list_l = arr[:n//2]
        sub_list_r = arr[(n//2):]

        merge_sort(sub_list_l)
        merge_sort(sub_list_r)

        # Przebieg lewo i prawo
        i = 0
        j = 0

        # iterator głównej listy
        k = 0

        while i < len(sub_list_l) and j < len(sub_list_r):
            if sub_list_l[i] <= sub_list_r[j]:
                arr[k] = sub_list_l[i]
                i += 1
            else:
                arr[k] = sub_list_r[j]
                j += 1
            k += 1

        while i < len(sub_list_l):
            arr[k] = sub_list_l[i]
            i += 1
            k += 1

        while j < len(sub_list_r):
            arr[k] = sub_list_r[j]
            j += 1
            k += 1
    return arr

# lista
tab = func.fill_list(11)

print(f"Lista: {tab}")

print(f"Posortowana Lista: {merge_sort(tab)}")



