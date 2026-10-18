def factorial(n):
      if n == 0 :
          return 1
      else:
          return n * factorial(n-1)

print(factorial(5))
print(factorial(3))

print("\n using for loop")
num = int(input("Enter the positive intger to get factorial:"))
res  = 1

for i in range(num + 1):
    if i == 0:
        continue
    elif i > num:
        break
    else:
        res *= i
print(res)
