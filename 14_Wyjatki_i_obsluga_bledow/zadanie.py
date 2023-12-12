while True:
    try:
        inp = str(input("podaj liczbe"))
        for c in inp:
           suma += inct(c)
        print(suma)

        if inp == "":
            break

    except IndexError as e:
            print(e)
    except ValueError as e:
            print("In Value Error")
            print(e)
    except Exception as e:
            print("In Exception")
            print(e)
    else:
            print("Koniec")
    finally:
            print("Finally")
print()

