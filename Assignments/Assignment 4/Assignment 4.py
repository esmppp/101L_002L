import random
def play_again():
    userInput = input("Do you want to play again? ==> ")
    while not(userInput.upper() == "YES" or userInput.upper() == "Y" or userInput.upper() == "N" or userInput.upper() == "NO"):
        print()
        print("You must enter Y/YES/N/NO to continue. Please try again")
        userInput = input("Do you want to play again? ==> ")
    if userInput.upper() == "YES" or userInput.upper() == "Y":
        return True
    else:
        return False

def get_wager(bank):
    wagers = int(input("How many chips do you want to wager ==> "))
    while not(0<wagers<=bank):
        if(wagers <= 0):
            print("The wager amount must be greater than 0. Please enter again.")
        elif(wagers>bank):
            print("The wager amount cannot be greater than how much you have. ", bank)
        wagers = int(input("How many chips do you want to wager ==> "))
    return wagers

def get_slot_results():
    return random.randint(1,10),random.randint(1,10),random.randint(1,10)
        
def get_matches(reela, reelb, reelc):
    if(reela == reelb and reelb == reelc):
        return 3
    elif(reela == reelb or reela == reelc or reelc == reelb):
        return 2
    else:
        return 0

def get_bank():
    chipsHeld = int(input("How many chips do you want to start with? ==> "))
    while not(0<chipsHeld<=100):
        if(chipsHeld<=0):
            print("Too low a value, you can only choose 1 -100 chips")
        elif(chipsHeld>100):
            print("Too high a value, you can only choose 1 -100 chips")
        chipsHeld = int(input("How many chips do you want to start with? ==> "))
    return chipsHeld

def get_payout(wager, matches):
    if(matches == 3):
        return 10*wager-wager
    elif(matches == 2):
        return 3*wager-wager
    elif(matches == 0):
        return -wager


player = True
numRuns = 0
maxChips = -500
while player:
    if(numRuns == 0):
        chipsHeld = get_bank()
        startingChips = chipsHeld
    if(chipsHeld > maxChips):
        maxChips = chipsHeld
    numRuns += 1
    wage = get_wager(chipsHeld)
    #Gets the spin and checks for matches
    num1, num2, num3 = get_slot_results()
    print("Your spin", num1, num2, num3)
    match = get_matches(num1,num2,num3)
    print("You matched", match, "reels")
    paid = get_payout(wage, match)
    print("You won/lost", paid)
    chipsHeld += paid
    print("Current bank", chipsHeld)
    print()
    if(chipsHeld == 0):
        print("You lost all", startingChips,"in", numRuns, "spins\nThe most chips you had was", maxChips)
        player = play_again()
        numRuns = 0
        maxChips = -500
    


    
