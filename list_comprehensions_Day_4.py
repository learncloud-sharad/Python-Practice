l1 = [1,2,3,4,5,6,7,8,9,10]

squares  = [num ** 2 for num in l1]
print(squares)

even_number  = [num for num in range(1,101) if num % 2 == 0]
print(even_number)

words = ["apple", "banana", "cherry","kiwi","mango","pineapple" ]
length_of_words = {word: len(word) for word in words}
print(length_of_words)


# square of even number and qube of odd number from  1 to 5
even_odd = [i ** 2  if i % 2 == 0  else i ** 3 for i in range(1,51) if i % 2 != 0]
print(even_odd)

l1 = ['aaa','bbbb','ccc','ddddddd','eee','ffffff']
cap_magic = [ch.upper() if len(ch) <= 3 else ch.capitalize() for ch in l1]
print(cap_magic)

salaries = [6000,5000,3000,7000,4000,8000,9000,2000]
apprisal = {f" Appresal for {sal} ": sal + sal * 0.20 if sal <=4000 \
            else  sal + sal * 0.10 \
           for sal in salaries}
for key, value in apprisal.items():
    print(f"{key} : {value}")