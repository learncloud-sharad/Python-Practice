#Exercise 1 : Number classification
#-----------------------------------------
try:
    num = float(input("Exercise 1 | Enter a number: "))

    if num > 0:
        if num % 2 == 0:
            print(num, "is an even number.")
        else:
            print(num, "is an odd number.")

    elif num < 0:
        print(num, "is a negative number.")

    else:
        print(num, "is zero.")

except ValueError:
    print("Not a valid number.")
