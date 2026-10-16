import random

print("Let's play Rock Paper Scissor!")

#Get user's choice

while True:
    user_choice = input("Enter your choice (Rock, Paper, Scissor): ").strip().lower()
    if user_choice in ["rock", "paper", "scissor"]:
        break
    else:
        print("Invalid choice, please try again.")
#Get Computer's choice

computer_choice = random.choice(["rock", "paper", "scissor"])
print("You'r choice is :",user_choice)
print("Computer choice is :",computer_choice)

#Determine the winner

if user_choice == computer_choice:
    print("It's a tie!")
elif (user_choice == "rock" and computer_choice == "scissor") or \
     (user_choice == "paper" and computer_choice == "rock") or \
     (user_choice == "scissor" and computer_choice == "paper") :
      print("You win!")
else:
    print("Computer wins!")