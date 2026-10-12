#Exercise 1 : Number classification
#-----------------------------------------

num  = int(input("Exercise 1 | Enter a number: "))

if num > 0:
    if num % 2 == 0:
        print(num, "is an even number.")
    else:
        print(num, "is an odd number.")
elif num < 0:
        print(num, "is an Negative number.")
else:
        print(num, "is not an even number.")

print("\n---------------------------------")