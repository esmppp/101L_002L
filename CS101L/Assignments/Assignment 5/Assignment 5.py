def get_school(string):
    if(string[5] == '1'):
        return "School of Computing and Engineering SCE"
    elif (string[5] == '2'):
        return "School of Law"
    elif (string[5] == '3'):
        return "College of Arts and Sciences"
    else:
        return "Invalid School"

def get_grade(string):
    if(string[6] == '1'):
        return "Freshman"
    elif (string[6] == '2'):
        return "Sophomore"
    elif (string[6] == '3'):
        return "Junior"
    elif(string[6] == '4'):
        return "Senior"
    else:
        return "Invalid Grade"

def character_value(string):
    alphabet = []
    for i in range(ord("A"), ord("Z")+1):
        alphabet.append(chr(i))
    return alphabet.index(string)

def get_check_digit(string):
    one = character_value(string[0]) * 1
    two = character_value(string[1]) * 2
    three = character_value(string[2]) * 3
    four = character_value(string[3]) * 4
    five = character_value(string[4]) * 5
    six = int(string[5]) * 6
    seven = int(string[6]) * 7
    eight = int(string[7]) * 8
    nine = int(string[8]) * 9
    total = (one+two+three+four+five+six+seven+eight+nine) % 10
    return total

def verify_check_digit(string):
    alphabet = []
    for i in range(ord("A"), ord("Z")+1):
        alphabet.append(chr(i))
    if(len(string) < 10):
        return(False, 'The length of the number given must be 10')
    for i in range(0,5):
        if string[i] not in alphabet:
            return (False, 'The first 5 characters must be A-Z, the invalid character is at {} is {}'.format(i,string[i]))
    for i in range(7,10):
        if not(string[i].isnumeric()):
            return(False, "The last 3 characters must be 0-9, the invalid character is at {} is {}".format(i, string[i]))
    if not(string[5] == '3' or string[5] == '2' or string[5] == '1'):
        return (False, "The sixth character must be 1 2 or 3")
    if not(string[6] == '3' or string[6] == '2' or string[6] == '1' or string[6] == '4'):
        return (False, "The seventh character must be 1 2 3 or 4")
    temp = get_check_digit(string)
    if int(temp) != int(string[9]):
        return (False, "Check Digit {} does not match the calculated value of {}.".format(string[9],temp))
    return (True, '')

userInput = input("Enter Library Card. Hit Enter to Exit ==> ")
while userInput != '':
    tupled = verify_check_digit(userInput)
    if tupled[0] == False:
        print("The Library card is invalid.")
        print(tupled[1])
    else:
        print("Library card is valid.")
        print("This card belongs to a student in", get_school(userInput))
        print("This card belongs to a", get_grade(userInput))
    print()
    userInput = input("Enter Library Card. Hit Enter to Exit ==> ")
