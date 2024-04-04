"""
Zadanie nr 2
Zaimplementuj algorytm mnożący dwie macierze kwadratowe zadane przez użytkownika.
Wejście: dwie macierze.
Wyjście: wynik mnożenia.
Oszacuj złożoność czasową algorytmu.
"""
import functions as func

# Złożoność obliczeniowa O(n^3)
def multiply_matrix(matrix_1, matrix_2):

    new_matrix = []

    n = len(matrix_1)
    for c in range(n):
        temp_list = []
        for a in range(n):
            sum = 0
            for b in range(n):
                sum += matrix_1[c][b] * matrix_2[b][a]
            temp_list.append(sum)
        new_matrix.append(temp_list)
    return new_matrix


"""
dimension = 2

matrix_1 = func.create_matrix(dimension)
matrix_2 = func.create_matrix(dimension)

print(f"Matrix_1: {func.show_matrix(matrix_1)}")
print(f"Matrix_2: {func.show_matrix(matrix_2)}")

# Złożoność obliczeniowa O(n^3)
print(f"Multiplayed matrix: {func.show_matrix(multiply_matrix(matrix_1, matrix_2))}")
"""
