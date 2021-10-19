mpg = 1
while not(0<mpg<=100):
    try:
        mpg = int(input("Enter the minimum mpg ==> "))
        if(mpg<=0):
            print('Fuel economy given must be greater than 0')
        if(mpg >=100):
            print('Fuel economy must be less than 100')
        mpg = int(input("Enter the minimum mpg ==> "))
    except:
        print("You must enter a number for the fuel economy")
fileName = ''
myFile = ''
while not(fileName != 'vehicle2.txt' or fileName != 'vehicles.txt'):
    try:
        fileName = input('Enter the name of the input vehicle file ==> ')
        myFile = open(fileName,'r')
    except:
        print('Could not open file', fileName)

lines = myFile.readlines()
listOfCars = {}
for line in lines:
    tempList = line.split('\t')
    #make = year, model, combinedmpg
    listOfCars[tempList[1]] = [tempList[0],tempList[2],tempList[7]]

for key in listOfCars:
    if listOfCars[key][2] >= mpg:
        print("{:<40}{:<40}{:<40}{:>10}".format(listOfCars[key][0],key,listOfCars[key][1]),listOfCars[key][2])

