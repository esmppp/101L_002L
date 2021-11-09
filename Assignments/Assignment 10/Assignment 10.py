def importingFile():
    notRight = True
    while notRight:
        try:
            fileName = input("Enter the name of the file to open ")
            myFile = open(fileName, "r")
            return myFile
        except:
            print("Could not open file", fileName, "\nPlease try again\n")

myFile = importingFile()
totalText = myFile.read()
for i in totalText:
    if i not in "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM ":
        totalText = totalText.replace(i,'')
    if i in "~`_-+={[}]|\:;\"\'<,>.?/!@#$%^&*()-":
        totalText = totalText.replace(i,"")

listText = totalText.split(" ")
dictText = {}
for i in listText:
    if i in dictText:
        dictText[i] += 1
    else:
        dictText[i] = 1
if '' in dictText:
    dictText.pop('')
sortedDict = sorted(dictText.items(), key=lambda kv: kv[1], reverse=True)
#print(sortedDict, "\n\n\n")
print("Most frequently used words")
print("{:<5}{:>15}{:>20}".format("#","Word","Freq."))
print("{:=<40}".format(''))
counter = 0
totalCounter = 0
while totalCounter < 10:
    if len(sortedDict[counter][0]) > 3:
        print("{:<5}{:>15}{:>20}".format(1+counter,sortedDict[counter][0],sortedDict[counter][1]))
        totalCounter += 1
    counter += 1
oneTime = 0
threeOrLess = 0

for i in dictText:
    if dictText[i] == 1:
        oneTime += 1
    if len(i) <= 3:
        threeOrLess += dictText[i]

print()
print("There are {} words that occur only once.".format(oneTime))
print("There are {} unique words in the document.".format(threeOrLess))
