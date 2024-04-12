"""
 Zadanie nr 1:
Dla następujących ciągów liczbowych:
wykonaj:
1. zaimplementuj (rekurenycjny) algorytm wyliczający wartość ntego elementu ciągu,
2. analitycznie wyznacz wzór na wartość ntego elementu ciągu (np. indukcyjnie),
3. napisz procedurę weryfikującą poprawność zaimplementowanej rekurencji (wyświetlającą i porównującą
wynik numeryczny i analityczny) dla N pierwszych elementów ciągu (N zadane przez użytkownika).
Wejście: N.
Wyjście: zestawienie wartości wyliczanych algorytmem rekurencyjnym i ze wzoru.
"""


def sequence_one_r(n):
    if n == 0:
        return 1
    return 3**n + sequence_one_r(n-1)


def seqeunce_one_a(n):
    sum = 1
    for a in range(1, n+1):
        sum += 3**a
    return sum


def sequence_two_r(n):
    if n == 0 or n == -1:
        return 0
    return n + sequence_two_r(n-2)


def sequence_two_a(n):
    temp = 0
    if n % 2 == 0:
        a = [x for x in range(2, n+2, 2)]
    else:
        a = [x for x in range(1, n+2, 2)]
    temp = sum(a)
    return temp


def sequence_three_r(n):
    if n==1:
        return 1
    if n==0:
        return 0
    return sequence_three_r(n-1) + sequence_three_r(n - 2)


def sequence_three_a(n):
   a, b = (1, 0)
   for i in range(2,n+1):
       temp = a
       a = a+b
       b = temp
   return a


n = 6
print(f"Dla liczby: {n} -> pierwszy ciąg: rekurencyjnie: {sequence_one_r(n)} analitycznie: {seqeunce_one_a(n)}")
print(f"Dla liczby: {n} -> drugi ciąg: {sequence_two_r(n)} analitycznie: {sequence_two_a(n)}")
print(f"Dla liczby: {n} -> trzeci ciąg: rekurencyjnie: {sequence_three_r(n)} analitycznie: {sequence_three_a(n)}")