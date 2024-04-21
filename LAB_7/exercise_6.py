"""
Zadanie nr 5 – RSA
Zaimplementuj algorytm RSA. Zaszyfruj nim (i odszyfruj) przykładowe teksty. W razie potrzeby, automatycznie dziel tekst na mniejsze, osobno szyfrowane części.
Wejście: tekst do zaszyfrowania/odszyfrowania.
Wyjście: zaszyfrowany/odszyfrowany tekst; klucz prywatny i klucz publiczny.
"""
import random
import exercise_3 as ex3


def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = extended_gcd(b % a, a)
        return gcd, y - (b // a) * x, x

def mod_inverse(e, phi):
    gcd, x, _ = extended_gcd(e, phi)
    if gcd != 1:
        raise Exception("Brak odwrotności modulo")
    else:
        return x % phi


def find_relative_prime(phi):
    e = 2
    while True:
        if ex3.enwd(e, phi) == 1:
            return e
        e += 1

def create_rsa_key():
    p = 19
    q = 17
    phi = (p - 1) * (q - 1)
    n = p * q
    e = find_relative_prime(phi)
    d = mod_inverse(e, phi)
    public_key = [e, n]
    private_key = [d, n]
    return public_key, private_key


def encrypt_message(message, e, n):
    encrypted_message = []
    for char in message:
        t = ord(char)
        if 0 < t < n:
            encrypted_char = pow(t, e, n)
            encrypted_message.append(encrypted_char)
        else:
            print("Znak '{}' nie spełnia warunku 0 < t < n i zostanie pominięty.".format(char))
    return encrypted_message


def decrypt_message(encrypted_message, d, n):
    decrypted_message = []
    for encrypted_char in encrypted_message:
        decrypted_char = pow(encrypted_char, d, n)
        decrypted_message.append(chr(decrypted_char))
    return ''.join(decrypted_message)




public, private = create_rsa_key()

wiadomosc = encrypt_message("duuupsko jebac ", public[0], public[1])
print(f"wiadomosc {wiadomosc}")
print(f"dekryptowana {decrypt_message(wiadomosc, private[0], private[1])}")






