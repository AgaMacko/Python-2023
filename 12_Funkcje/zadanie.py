stworzyc słownik { 'first': funkcja1, 'second': funkcja2 },
wczytać przez input klucz, wywołać funkcję


stworzyc funckcję alphabet_range działająca
jak range ale dla liter (z trzema parametrami - start, end, step)
przykład: alphabet_range('E') -> ['A', 'B', 'C', 'D'] - albo jeszcze lepiej generator
użyć
ord - podaje kod calkowity danego znaku
chr - podaje znak odpowiadający danemu kodowi całkowitemu

def alphabet_range(start, end, step):
    return [x for x in range(ord(start), ord(end), step)]

alphabet_range("a", "f",1)