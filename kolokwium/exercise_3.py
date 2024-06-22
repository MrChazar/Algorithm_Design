# Zadanie 3
import exercise_1 as ex1


# a) Implementacja sortowania przez zliczanie
def counting_sort(arr):
    # Znalezienie maksymalnego i minimalnego wieku
    max_age = max(arr, key=lambda x: x[1])[1]
    min_age = min(arr, key=lambda x: x[1])[1]
    range_count = max_age - min_age + 1

    # Inicjalizacja tablicy zliczającej i tablicy wynikowej
    count = [0] * range_count
    output = [None] * len(arr)

    # Zliczanie wystąpień wieku
    for student in arr:
        count[student[1] - min_age] += 1

    # Modyfikacja tablicy zliczającej, aby przechowywała pozycje
    for i in range(1, range_count):
        count[i] += count[i - 1]

    # Tworzenie tablicy wynikowej na podstawie tablicy zliczającej
    for student in reversed(arr):
        output[count[student[1] - min_age] - 1] = student
        count[student[1] - min_age] -= 1

    return output


# b) Implementacja algorytmu Quicksort dla studentów
def quicksort(arr, low, high, step_by_step=False):
    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j][3] <= pivot[3]:  # Sortowanie według ocen (element 3)
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def _quicksort(arr, low, high, step_by_step, step_count):
        if low < high:
            pi = partition(arr, low, high)
            if step_by_step:
                step_count += 1
                print(f"Krok {step_count}:")
                ex1.show_students(arr)
                print("\n")
            _quicksort(arr, low, pi - 1, step_by_step, step_count)
            _quicksort(arr, pi + 1, high, step_by_step, step_count)

    step_count = 0
    _quicksort(arr, low, high, step_by_step, step_count)



if __name__ == "__main__":
    # Wczytanie danych
    students = ex1.read_students()
    print("Nasi studenci:")
    ex1.show_students(students)

    # posortowane przez zliczenie
    sorted_stack = counting_sort(students)

    # wyświetlanie posortowanej przez zliczanie
    print("wyświetlanie posortowanej przez zliczanie")
    ex1.show_students(sorted_stack)

    print("sortowanie przez quick sort")
    # posortowanie przez quicksort
    quicksorted_stack = quicksort(students, 0, len(students) - 1, step_by_step=True)