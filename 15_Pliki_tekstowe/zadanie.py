
first_line = None


with open('data//foods.csv') as f:
    for l in f:
        if first_line is None:
            first_line = l.strip().split(',')
        else:
            dane = l.strip().split(',')
            print(first_line)
            print(dane)
            slownik = list(zip(first_line, dane))
            print(slownik)

        print(l.strip)
