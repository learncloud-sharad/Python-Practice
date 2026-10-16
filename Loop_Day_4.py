l1 = [1,2,3,4,5,6,7,8,9,10]

#print all element except 3 and 5 and all elements after 7.

for i in l1:
    if i == 3 or i == 5:
        pass
    elif i > 7:
        break
    else:
        print(i, end=" ")



print("\n##### While Loop ###")
# Exit number is : 12
while True:
    user_input = int(input("Enter a integer number: "))
    if user_input == 12:
        print("Good Bye")
        break
    else:
        print(user_input, end="\n ")


##### from 1 to 100 print all number except multiplications of 3 and
##### skip all numbers after 70
print("\n")
for i in range(1,101):
    if i%3 == 0 :
        continue
    elif i > 70:
        break
    else:
        print(i, end="\t ")
