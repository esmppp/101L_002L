def month_from_number(num):
    month = num-1
    months = ['January', "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", 'December']
    if 0<=month<=11:
        return months[month]
    else:
        raise ValueError

def read_in_file(name):
    try:
        myFile = open(name, encoding='utf-8')
        firstList = myFile.readlines()
        nextList = []
        for i in firstList:
            nextList.append(i.split(','))
        myFile.close()
        nextList.pop(0)
        return nextList
    except:
        print('Invalid File, please try again.')

def create_reported_data_dict(list):
    dict1 = {}
    for i in list:
        if i[1] in dict1:
            dict1[i[1]] = dict1[i[1]] + 1
        else:
            dict1[i[1]] = 1
    return dict1

def create_reported_month_dict(list):
    dict2 = {}
    for i in list:
        if i[1][:2] in dict2:
            dict2[i[1][:2]] = dict2[i[1][:2]] +1
        else:
            dict2[i[1][:2]] = 1
    return dict2

def create_offense_dict(list):
    dict3 = {}
    for i in list:
        if i[7] in dict3:
            dict3[i[7]] = dict3[i[7]] +1
        else:
            dict3[i[7]] = 1
    return dict3

def create_offense_by_zip(list):
  dict4 = {}
  for i in list:
    test1 = i[7]
    test2 = i[13]
    if test1 in dict4:
      if test2 in dict4[test1]:
        dict4[test1][test2] = dict4[test1][test2] + 1
    else:
      dict4[test1] = {test2: 1}
  return dict4

sentinel = 0
while sentinel == 0:
    try:
        fileName = input("Enter file name: ")
        testOpen = open(fileName, 'r')
        crimeList = read_in_file(fileName)
        sentinel = 1
    except:
        print("Could not find the file specified. {} not found". format(fileName))
print()
crimeMonthBig = create_reported_month_dict(crimeList)
highest = 0
key = ''
for i in crimeMonthBig:
    if crimeMonthBig[i] > highest:
        highest = int(crimeMonthBig[i])
        key = int(i)
print("The month with the highest # of crime rates is {} with {} offenses".format(month_from_number(key),highest))

crimeBig = create_offense_dict(crimeList)
highest = 0
key = ''
for i in crimeBig:
    if crimeBig[i] > highest:
        highest = crimeBig[i]
        key = i
print("The offense with the highest # of crimes is {} with {} offenses".format(key,highest))
print()

s2 = 0
while s2 == 0:
    try:
        crimeName = input("Enter an offense: ")
        if(crimeName not in crimeBig):
            raise ValueError
        s2 = 1
    except:
        print("Not a valid offense found, please try again")
print()
print('{} offenses by Zip Code'.format(crimeName))
print('{:<15}{:>15}'.format('Zip Code','# Offenses'))
print('{:=<30}'.format(''))
crimesAreaCode = create_offense_by_zip(crimeList)
for i, j in crimesAreaCode.items():
  if i == crimeName:
    for key in j:
      print('{:<15}{:>15}'.format(key,j[key]))