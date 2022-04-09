import random
user_wins = 0
computer_wins = 0

options = ['rock', 'paper', 'scissor']
while True:
    user_input = input("Type Rock/Paper/Scissor or Q to quit the game? ").lower()
    if user_input == "q":
        break
    if user_input not in options:
        print("Type Rock, Paper or scissor only")
        continue
    random_number = random.randint(0, 2)
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")
    if user_input == "rock" and computer_pick == "scissor":
        print("Congratulation!!! You win....")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("Congratulation!!! You win....")
        user_wins += 1
    elif user_input == "scissor" and computer_pick == "rock":
        print("Congratulation!!! You win....")
        user_wins += 1
    elif user_input == computer_pick:
        print("Both picked same... Its a draw")
        continue
    else:
        print("Computer wins!!!!")
        computer_wins += 1




print("Score: Computer (",computer_wins, ") You (", user_wins, ")" )
print("Goodbye!!!!!!!")