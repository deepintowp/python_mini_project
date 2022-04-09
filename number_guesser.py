import random
top_range_number  = input("Type a number? ")
if top_range_number.isdigit():
    top_range_number = int(top_range_number)
    if top_range_number <= 0:
        print("Please type grater than Zero.")
        quit()

else:
    print("Please type number only.")
    quit()


random_number = random.randint(0, top_range_number) 
gusses = 0
while True:
    gusses += 1
    user_guess = input("Make a guess? ");
    if user_guess.isdigit():
        user_guess = int(user_guess)


    else:
        print("Please type number only.")
        continue #bring back to to of the loop
    if user_guess == random_number:
        print("You got it.")
        break #quit out from loop
    else:
        if user_guess > random_number:
            print("You are above the number")
            continue
        else: 
            print("You are below the number")
            continue

       
print("You got it right in ", gusses , "gusses")