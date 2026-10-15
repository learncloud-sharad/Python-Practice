from elif_Simple_Example_Day_2 import attempts

print("#### For LOOP ####")
correct_username = "Bahubali"
correct_password = "Mahismati@123"
username = input("Enter Username: ")
password =  input("Enter your password: ")

for i in range(3,1,-1) :
    if password == correct_password and username == correct_username :
        print("Login Successful")
        break
    else:
        print(f"Login Failed | Wrong Password | Retries remaining: {i-1}")
        if i == 1:
            print("Login Failed")
        else:
            username = input("Enter Username: ")
            password = input("Enter your password: ")

