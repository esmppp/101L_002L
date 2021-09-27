print("Welcome to the Flarsheim Guesser!")
userInput = 'y'
while userInput.upper() == 'Y':
    print("Please think of a number between and including 1 and 100.\n")
    rem1 = int(input("What is the remainder when your number is divided by 3 ?"))
    while not (0 <= rem1 < 3):
        if(rem1 >=3):
            print("The value entered must be less than 3")
            rem1 = int(input("What is the remainder when your number is divided by 3 ?"))
        elif(rem1 < 0):
            print("The value entered must be 0 or greater")
            rem1 = int(input("What is the remainder when your number is divided by 3 ?"))
    print()
    rem2 = int(input("What is the remainder when your number is divided by 5 ?"))
    while not (0 <= rem2 < 5):
        if(rem2 >=5):
            print("The value entered must be less than 5")
            rem2 = int(input("What is the remainder when your number is divided by 5 ?"))
        elif(rem2 < 0):
            print("The value entered must be 0 or greater")
            rem2 = int(input("What is the remainder when your number is divided by 5 ?"))
    print()
    rem3 = int(input("What is the remainder when your number is divided by 7 ?"))
    while not (0 <= rem3 < 7):
        if(rem3 >=7):
            print("The value entered must be less than 7")
            rem3 = int(input("What is the remainder when your number is divided by 7 ?"))
        elif(rem3 < 0):
            print("The value entered must be 0 or greater")
            rem3 = int(input("What is the remainder when your number is divided by 7 ?"))
    numGuessed = -5
    for i in range(0,101):
        if(i%3==rem1):
            if(i%5 == rem2):
                if(i%7 == rem3):
                    numGuessed = i
    print("Your number was ", numGuessed)
    print("How amazing was that?\n")
    userInput = input("Do you want to play again? Y to continue, N to quit  ==> ")
    while not(userInput.upper() == 'Y' or userInput.upper() == 'N'):
        userInput = input("Do you want to play again? Y to continue, N to quit  ==> ")