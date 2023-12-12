# Zadania

- Stworzyć *list comprehension* na podstawie jednej listy z liczbami całkowitymi, ale z elementami o 6 większymi
- Stworzyć *list comprehension* tupli składających się z w/w liczb całkowitych i ich reprezentacji jako napis
  - np. `[(1, "1"), (2, "2")]`
- biorąc słownik `{"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Minivan": 1600, "Van": 2400, "Semi": 13600, "Bicycle": 7, "Motorcycle": 110}` stworzyć list comprehension nazw pojazdów cięższych niż 5000
  - Nazwy podać dużymi literami (*uppercase*)
`

- List comprehension


(x * x for x in range(10))

[x for x in range(10)]

[x * x for x in range(10)]

[x for x in range(int) if x + (x +6)  == 0]

[x * x for x in str(range(10)) if x + 2 == 0]

[(x, y, x * y) for x in range(3) for y in range(4)]

{x for x in range(str(x)) if x + (x+6)}

{x // 2 for x in range(10)}

{x: x * x for x in range(10) if x % 2 == 0}

[(x, str(x)) for x in range(10)]

dictionary = {"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Minivan": 1600, "Van": 2400, "Semi": 13600, "Bicycle": 7, "Motorcycle": 110}

[x for x in dictionary.keys() if dictionary[x] > 5000]
print(h)



kwadraty = []

for i in range(10):
    if i % 2 == 0:
        kwadraty.append(i * i)

print(kwadraty)

print([i * i for i in range(10) if i % 2 == 0])

def alphabet_range()


---------
    def alphabet_range(start="A", end="z", step=1):
        return (chr(x) for x in range(ord(start), ord(end), step))

    alphabet_range("a", "f", 1)
    list(alphabet_range(end="M")