n = 5

while n > 0:
    print(n)
    n -= 1



for a in range(1, 100):
    b = a % 10
    c = a // 10
    i = b + c
    if (i % 7 == 0 and i % 2 == 0):
        print(f"{a} liczba jest dobra")

n = 8
while n > 0:
    n -= 1
    if n % 2 == 0:
        print(f'{n} tik')
        continue
    print(f'{n} tak')


n = 8
while n > 0:
    n -= 1
    if n % 2 == 0:
        print(f'{n} tik')
        continue

    if n < 3:
        break
    print(f'{n} tak')

n = 8
while n > 0:
    n -= 1
    if n % 2 == 0:
        print(f'{n} tik')
        continue

    if n < 3:
        break
    print(f'{n} tak')
else:
    print('Koniec')

n = 15
while n > 0:
    n -= 1
    if n % 2 == 0:
        print(f'{n} tik')
        continue

    print(f'{n} tak')
else:
    print('Koniec')

