try:
    n1, n2 = eval(input("Enter two numbers seperated by a comma: "))
    n = n1/n2
    print("Result is: ", n)

except ZeroDivisionError:
    print("Division by 0 is an error")

except SyntaxError:
    print("Comma is missing")

except: # this is a ValueError
    print("Wrong input")
else:
    print("No exceptions")
finally:
    print("This will get executed no matter what")
