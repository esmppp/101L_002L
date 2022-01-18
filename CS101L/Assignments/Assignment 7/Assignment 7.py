# Ethan Miller
# CS101L
# esmppp@umsystem.edu
# Fuel Economy (Lab Week 8 - File handling, Try except)
# Special handling: If a file is not found in openingFile(), then an except is called and the code continues to run
def checkMPG():
    mpg = 0
    while not(0<mpg<100):
        try:
            mpg = int(input("Enter the minimum mpg ==> "))
            if(0>=mpg):
                print("Fuel economy given must be greater than 0")
            if(100<=mpg):
                print("Fuel economy must be less than 100")
            if(0<mpg<100):
                return int(mpg)
        except:
            print("You must enter a number for the fuel economy")

def openingFile():
    check = True
    while check:
        try:
            fileName = input("Enter the name of the input vehicle file ==> ")
            myFile = open(fileName,'r')
            return myFile
        except:
            print("Could not open file", fileName)

def writingFile():
    check = True
    while check:
        try:
            out = input("Enter the name of the file to output to ==> ")
            myOutput = open(out,'r+')
            return myOutput
        except IOError:
            print("There is an IO Error", out)
        except:
            print("There is an IO Error", out)

mpg = checkMPG()
print()
#Need to figure out how to open a file with Visual Studio Code
myFile = openingFile()
print()
myOutput= writingFile()

lines = myFile.readlines()
for row in lines[1:]:
    try:
        tempList = row.split('\t')
        #print(tempList)
        mpgComp = tempList[7]
        mpgComp = int(mpgComp)
        if mpgComp >= mpg:
            outing = '{:<40}{:<40}{:<40}{:>10.3f}'.format(tempList[0], tempList[1], tempList[2], mpgComp)
            #print(outing)
            myOutput.write(outing + '\n')
    except:
        print("Could not convert value", tempList[7], 'for', tempList[0], tempList[1], tempList[2])

myFile.close()
myOutput.close()