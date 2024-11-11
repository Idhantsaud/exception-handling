option = True
while option:
    try:
        a = int(input("Enter a number: "))
        while a%2 == 0:
            print("Bye")
        option = False
    except ValueError as ex:
        print("Exception: ", ex)