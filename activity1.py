try:
    n = int(input("Enter number: "))
    print("The number you entered is: ", n)

except ValueError as ex:
    print("Exception: ", ex)