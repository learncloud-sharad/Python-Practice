my_list = [1, 2, 3,'Sharad',-6,5.4]

print(my_list)
print("Third element ",my_list[2])
print("Slice ",my_list[2:6])

# appending
my_list.append('Github')
print(my_list)

# removing element from list
my_list.remove(-6)
print(my_list)

# using pop()
popped_item = my_list.pop()
print("Popped Item :  ",popped_item)
print(my_list)

# len of list
print("Length of list : ",len(my_list))
