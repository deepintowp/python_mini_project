print("Welcomto my computer quiz.")
answer = input("Do you want to play a game? ").lower()

if answer != "yes":
    quit()
print("Ok lets play :) ")
score = 0
answer = input("What CPU stands for? ").lower()

if answer == "central processing unit":
    print("Correct! ")
    score +=1
else:
    print("Incorrect!")



answer = input("What GPU stands for? ").lower()
if answer == "graphic processing unit":
    print("Correct! ")
    score +=1
else:
    print("Incorrect!")

answer = input("What IP stands for? ").lower()
if answer == "internet protocol":
    print("Correct! ")
    score +=1
else:
    print("Incorrect!")

answer = input("What FTP stands for? ").lower()
if answer == "file transfer protocol":
    print("Correct! ")
    score +=1
else:
    print("Incorrect!")

print("You got "+str(score)+ " question right ( "+str((score/4)*100)+" % ) ")