nums = [2,0,-1,4,5,-5,7,6]

result = [f"{i} is a "+"Positive Number" if i > 0
              else  f"{i} is a "+"Negative Number" if i < 0
              else f"{i} is a Zero" for i in nums]
print(result)

magic = ["FizzBuzz"if (i % 3 == 0 and  i % 5 == 0)
          else "Fizz" if i % 3 == 0
          else "Buzz" if i % 5 == 0
          else i
          for  i in range(1,51) if i % 3 == 0 ]
print(magic)