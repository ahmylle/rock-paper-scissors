# 1. Import the random module.

import random 
play_again=True
print("welcome to rock paper scissoes!")
while play_again:

# 2. Generate a random number between 1 and 3 and set it equal to a variable called computer (hint: use the randint() function) 
    reptar = random.randint(1,3)
    print (reptar)

    # 3. Using input, get the user's choice where 1 is rock, 2, paper, and 3 is scissors. Store the user's input in a variable called user.
    choice =int(input ("enter \n 1 for rock \n 2 for paper \n 3 for scissors:"))

    # 4. Use if-statements to determine the winner of the game and print the result.
    # If the computer and the user choose the same option, print "It's a tie!". If the computer wins, print "Computer wins!". If the user wins, print "You win!". 


    # paper (2) beats rock (1)
    # rock (1) beats scissors (3)
    # scissors (3) beats paper (2)
    print ("reptar chose", reptar)

    if reptar == choice:
        print("its a tie")
    elif reptar == 2 or choice == 1:
        print ("you lose")
    elif reptar==1 and choice ==2:
        print ("you lose")
    elif reptar==3 and choice==2:
        print ("you lose")
    elif choice >3  or choice < 1:
        print("that option is not allowed")
    else:
        print("you win")

        user_input= input("do you want to play again")
        if user_input== "no":
            play_again=False

print()
print("thanks for playing") 