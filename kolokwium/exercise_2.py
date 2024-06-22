# Zadanie 2
import exercise_1 as ex1


# algorytm rekurencyjny znajdujacy największa liczbe
def biggest_element(A, n):
    if (n == 1):
        return A[0]
    return max(A[n - 1], biggest_element(A, n - 1))


# algorytm rekurencyjny znajdujacy druga najwieksza liczbe
def second_biggest_element(A, n):
    A.remove(biggest_element(A, n))
    return biggest_element(A, n-1)

# algorytm rekurencyjny znajdujacy mediane
def median(A, N):
    A.sort()

    def median_h(A, left, right):
        length = right - left + 1
        mid = left + (length // 2)

        if length % 2 == 0:
            return (A[mid - 1] + A[mid]) / 2
        else:
            return A[mid]
    return median_h(A, 0, N - 1)


if __name__ == "__main__":
    # Wczytanie danych
    students = ex1.read_students()
    print("Nasi studenci:")
    ex1.show_students(students)

    # A) Najwieksza ocena
    grades = students[::-1][::-1]
    # Wyszukanie ocen studentów
    grades = [student[3] for student in students]

    # Największa ocena
    highest_grade = biggest_element(grades[:], len(grades))
    print(f"Największa ocena: {highest_grade}")
    print(f"Student z tą oceną: {[student for student in students if student[3] == highest_grade]}")

    # Druga największa ocena
    second_highest_grade = second_biggest_element(grades[:], len(grades))
    print(f"Druga największa ocena: {second_highest_grade}")
    print(f"Student z drugą największą oceną: {[student for student in students if student[3] == second_highest_grade]}")

    # Mediana Ocen
    median = median(grades[:], len(grades))
    print(f"Mediana: {median}")
