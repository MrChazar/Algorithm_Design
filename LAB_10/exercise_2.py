"""
Zadanie nr 2 – wyszukiwanie binarne
Zaimplementuj kolejny algorytm wyszukiwania robota na liście.
1. Pobierz od użytkownika parametr robota (TYP, CENA, ZASIĘG, KAMERA). Posortuj listę robotów względem
zadanego parametru. Wykorzystaj wbudowaną funkcję sort.
2. Zaimplementuj algorytm wyszukujący robota po liście dopuszczalnych wartości wybranego parametru.
Zadanie wykonaj przy założeniu, że lista robotów jest odpowiednio posortowana. Algorytm zwraca
parametry pierwszego znalezionego robota lub „brak”, jeśli robota nie znajdzie.
Wejście: lista robotów (wczytywana z pliku), wybrany parametr szukanego robota i lista wartości.
Wyjście: lista parametrów znalezionego robota lub „brak”.
Uwaga: realizując zadanie zaadoptuj (być może wielokrotnie) algorytm wyszukiwania binarnego.
"""
import LAB_9.exercise_1 as rob


def remove_robot(robots, removed_robots):
    removed = robots.pop(0)
    removed_robots.append(removed)
    print(f"Robot o parametrach: {removed} usunięty")


def clear_robots(robots, removed_robots):
    while robots != []:
        a = robots.pop(0)
        removed_robots.append(a)
    print("Roboty usunięte razem z tymi z oczyszczenia")
    rob.show_robots(removed_robots)


def binary_search_robots(robots, param_index, value):
    low, high = 0, len(robots) - 1
    while low <= high:
        mid = (low + high) // 2
        mid_value = robots[mid][param_index]

        if mid_value == value:
            # Find the first occurrence if there are duplicates
            while mid > 0 and robots[mid - 1][param_index] == value:
                mid -= 1
            return robots[mid]
        elif mid_value < value:
            low = mid + 1
        else:
            high = mid - 1
    return "brak"


def search_robot(parameter, value_a, value_b):
    param_map = {'Type': 0, 'Price': 1, 'Range': 2, 'Camera': 3}
    param_index = param_map[parameter]

    # Ensure value_a and value_b are appropriate types
    if parameter != 'Type':
        value_a = float(value_a)
        if value_b:
            value_b = float(value_b)

    # Sort the robots list by the selected parameter
    stack.sort(key=lambda x: x[param_index])

    if value_b == "":
        # Binary search for a single value
        return binary_search_robots(stack, param_index, value_a)
    else:
        # Binary search for the range [value_a, value_b]
        low, high = 0, len(stack) - 1
        result = "brak"

        while low <= high:
            mid = (low + high) // 2
            mid_value = float(stack[mid][param_index])

            if value_a <= mid_value <= value_b:
                # Find the first occurrence within the range
                while mid > 0 and float(stack[mid - 1][param_index]) >= value_a:
                    mid -= 1
                result = stack[mid]
                break
            elif mid_value < value_a:
                low = mid + 1
            else:
                high = mid - 1

        return result


stack = []
removed_stack = []

control = 'e'

while(control != 'q'):

    control = input("Możesz - dodać robota : a, usunąć robota: r, wczytać roboty: l, wyświetlić roboty: p, wyszukać robota: f , wyjść: q "
                    "Wybór:")
    if control == 'a':
        robot = rob.generate_robots(1)
        print(robot)
        stack.append(rob.add_robot(robot[0]))

    if control == 'r':
        remove_robot(stack, removed_stack)

    if control == 'l':
        stack += rob.read_robots()

    if control == 'p':
        rob.show_robots(stack)

    if control == 'f':
        parameter = input("Wybierz parametr: 'Type', 'Price', 'Range', 'Camera':")
        value_a = input("Pierwsza wartość:")
        value_b = input("Druga wartość:")
        print("Wynik:")
        print(search_robot(parameter, value_a, value_b))