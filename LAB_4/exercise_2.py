"""
Zaimplementuj program, który wypełni listę wartościami losowymi a następnie posortuje dane metodą bąbelkową,
"""
import functions as func

def bubble_sort(n):
    for i in range(len(n)):
        swapped = False
        for j in range(0, len(n) - i - 1):
            if n[j] > n[j + 1]:
                n[j], n[j + 1] = n[j + 1], n[j]
                swapped = True
        if swapped == False:
            break
    return n

tab = func.fill_list(10)
print(f"Lista: {tab}")

tab = bubble_sort(tab)
print(f"Posortowana {tab}")
