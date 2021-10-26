import statistics
def printMenu():
    print('{:^20}'.format("Grade Menu"))
    val = input("1 - Add Test\n2 - Remove Test\n3 - Clear Tests\n4 - Add Assignment\n5 - Remove Assignment\n6 - Clear Assignments\nD - Display Score\nQ - Quit\n\n==> ")
    while val.upper() not in ("123456DQ"):
        val = input("1 - Add Test\n2 - Remove Test\n3 - Clear Tests\n4 - Add Assignment\n5 - Remove Assignment\n6 - Clear Assignments\nD - Display Score\nQ - Quit\n\n==> ")
    return val

def addIt(score,lists):
    if score < 0:
        print("Could not add score")
    else:
        lists.append(float(score))

def removeIt(score,lists):
    if score in lists:
        lists.remove(score)
    else:
        print("Could not find that score to remove")

def clearIt(lists):
    lists.clear()

def maxi(lists):
    if len(lists) == 0:
        return 'n/a'
    else:
        return "{:.2f}".format(max(lists))

def mini(lists):
    if len(lists) == 0:
        return 'n/a'
    else:
        return "{:.2f}".format(min(lists))

def averages(lists):
    if len(lists) == 0:
        return 'n/a'
    else:
        total = 0
        for i in lists:
            total += float(i)
        total /= len(lists)
        return "{:.2f}".format(total)

def std(lists):
    if len(lists) == 0:
        return 'n/a'
    else:
        mean = sum(lists) / len(lists)
        variance = sum([((x - mean) ** 2) for x in lists]) / len(lists)
        stds = variance ** 0.5
        return "{:.2f}".format(stds)

def weighted():
    totalA = 0
    for i in assignList:
        totalA += float(i)
    if len(assignList)>0:
        totalA /= len(assignList)
    totalA *= .4
    totalT = 0
    for i in testList:
        totalT += i
    if len(testList)>0:
        totalT /= len(testList)
    totalT *= .6
    return ("{:.2f}".format(totalA + totalT))

def printScores():
    print("{:<15}{:>10}{:>10}{:>10}{:>10}{:>10}".format("Type","#","min","max","mean","std"))
    print("{:=<65}".format(''))
    print("{:<15}{:>10}{:>10}{:>10}{:>10}{:>10}".format("Tests", len(testList),mini(testList),maxi(testList),averages(testList),std(testList)))
    print("{:<15}{:>10}{:>10}{:>10}{:>10}{:>10}".format("Assignments", len(assignList),mini(assignList),maxi(assignList),averages(assignList),std(assignList)))
    print()
    print("The weighted score is",weighted())

testList = []
assignList = []

userInput = printMenu()
while userInput.upper() != 'Q':
    if userInput == '1':
        num = float(input("Enter the new Test score 0-100 ==> "))
        addIt(num,testList)
    elif userInput == '2':
        num = float(input("Enter the Test to remove 0-100 ==> "))
        removeIt(num,testList)
    elif userInput == '3':
        clearIt(testList)
    elif userInput == '4':
        num = float(input("Enter the new Assignment score 0-100 ==> "))
        addIt(num,assignList)
    elif userInput == '5':
        num = float(input("Enter the Assignment to remove 0-100 ==> "))
        removeIt(num,assignList)
    elif userInput == '6':
        clearIt(assignList)
    elif userInput.upper() == 'D':
        printScores()
    userInput = printMenu()