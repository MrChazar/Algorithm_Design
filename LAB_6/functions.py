import random


def create_matrix(n):
    matrix = []
    for a in range(n):
        list = fill_list(n)
        matrix.append(list)
    return matrix


def show_matrix(list):
    for a in range(len(list)):
        print(list[a])
    return None


def fill_list(n):
    return [random.randint(-10, 10) for _ in range(n)]



