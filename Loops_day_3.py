l1 = [1,2,3,4,5,6,7,8,9,10]
l2 = []
for i in l1:
    l2.append(i*i)
print(l1)
print(l2)

for k in l1:
    print(k+10 ,end="\t")
t =[]
for m in l1:
    if m % 2 == 0:
        t.append("Even")
    else:
        t.append("Odd")
print("\n",t)
print("\n\n While Loop\n")
#####################@@@  While Loop @@@#############################

fruits = ["apple", "banana", "cherry"]
i = 0
while i < len(fruits) :
    print(fruits[i-1],end="\t")
    i = i + 1
print("\nOut of loops")

print("\n#### Calculate the sq of each number\n")
l1 = [1,2,3,4,5,6,7,8,9,10]
i = 0
while i < len(l1):
    print(l1[i]*l1[i],end="\t")
    i = i + 1
print("\nOut of loops")


print("\n#### Salary Calculator\n")

salaries = [2000,5000,12000,1500,4300,6000,10000,1800]
i = 0
while i < len(salaries):
    if salaries[i] >= 3000:
        print(f"Increment of salary for {salaries[i]} is: {salaries[i] * 1.10:,.2f}")
    else:
        print(f"Increment of salary for {salaries[i]} is: {salaries[i] * 1.20:,.2f}")
    i = i + 1
print("\nOut of loops")
