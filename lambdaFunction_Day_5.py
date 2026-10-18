#sort List
data = [('John',25),('Doe',30),('Jane', 20)]

sorted_data = sorted(data,key = lambda x: x[1])
print(sorted_data)