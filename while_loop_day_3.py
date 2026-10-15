print("\n\n#### While LOOP ####")
correct_username = 'Sharad'
correct_password = 'Pass@123'
attempts = 0
while attempts <= 4 :
    username = input("Enter Username: ")
    password = input("Enter your password: ")
    if username == correct_username and password == correct_password   :
        print("Login Successful")
        break
    else:
        print(f"Login Failed | Wrong Password | Retries remaining: {attempts}")
        attempts = attempts + 1
        remaining_attempts = 4 - attempts
        print(f"Remaining Attempts: {remaining_attempts}")
        if remaining_attempts == 0 :
            print("You have reached  the maximum number of attempts, tray later :")
            break
