print("    ........ CALCULATOR ........            ")
while True:
    print("Enter 'Q' to quit ")
    print("Enter '+' to add two number ")
    print("Enter '-' to subtract two number ")
    print("Enter '*' to multiply two number ")
    print("Enter '/' to devide two number ")
    a = input("Enter operator  :")

    if a == "Q":
        break

    if a == "+":
        b = float(input("Enter first number :"))
        c = float(input("Enter second number :"))
        result = b + c
        print(result)

    elif a == "-":
        b = float(input("Enter first number :"))
        c = float(input("Enter second number :"))
        result = b - c
        print(result)

    elif a == "*":
        b = float(input("Enter first number :"))
        c = float(input("Enter second number :"))
        result = b * c
        print(result)

    elif a == "/":
        b = float(input("Enter first number :"))
        c = float(input("Enter second number :"))
        result = b / c
        print(result)

    else:
        print("Wrong input!!!")