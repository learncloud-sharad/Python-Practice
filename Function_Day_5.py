def addition(a,b):
    sum = a + b
    print(f"Sum of {a} and  {b} is {sum}\n")

addition(3,4)

### USer detials
def print_user_details(name,mobile=1234567890 ):
    print(f"\nName: {name}")
    print(f"Mobile: {mobile}")
print_user_details("Joe",2564897)
print_user_details("Alex")

############
print("\n Args")
def student_marks(rno=234, *marks,sname="NA"):
    print(f"Roll_no: {rno}")
    print(f"Marks: {marks}")
    print(f"Student Name: {sname}")

student_marks()
student_marks(2,84,45,64, sname="Sharad")