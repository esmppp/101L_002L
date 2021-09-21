########################################################################
##
## CS 101 Lab
## Program #2
## Name: Ethan Miller
## Email: esmppp@umsystem.edu
## Designation: Student
##
## PROBLEM : Describe the problem
## Here we are trying to calculate the grade of a student for the weighted CS 101 Lab.
## ALGORITHM : 
##      1. Write out the algorithm
print("**** Welcome to the Lab grade calculator ****\n")
name = input("Who are we calculating grades for? ==> ")
print()
lab = float(input("Enter the Labs grade? ==> "))

if(lab > 100):
    lab = 100
    print("The lab value should have been 100 or less. The grade has been changed to 100.")
elif(lab < 0):
    lab = 0
    print("The lab value should have been 0 or greater. The grade has been changed to 0.")
print()
exam = float(input("Enter the EXAMS grade? ==> "))

if(exam > 100):
    exam = 100
    print("The exam value should have been 100 or less. The grade has been changed to 100.")
elif(exam < 0):
    exam = 0
    print("The exam value should have been 0 or greater. The grade has been changed to 0.")
print()
attend = float(input("Enter the ATTENDANCE grade? ==> "))

if(attend > 100):
    attend = 100
    print("The attendance value should have been 100 or less. The grade has been changed to 100.")
elif(attend < 0):
    attend = 0
    print("The attendance value should have been 0 or greater. The grade has been changed to 0.")

total = lab*.7+exam*.2+attend*.1

if(total >= 90):
    grade = 'A'
elif(80 <= total < 90):
    grade = 'B'
elif(70 <= total < 80):
    grade = 'C'
elif(60 <= total < 70):
    grade = 'D'
elif(total < 60):
    grade = 'F'
print()
print("The weighted grade for", name, "is", total)
print(name, "has a letter grade of", grade)
print("\n**** Thanks for using the Lab grade generator ****")
## 
## ERROR HANDLING:
##      Any Special Error handling to be noted.  Wager not less than 0. etc
##      If lab, exam, or attend are assigned a variable higher than 100 they are assigned to 100 and a statement is printed to notify the user of the change
##      If lab, exam, or attend are assigned a variable lower than 0 they are assigned to 0 and a statement is printed to notify the user of the change
## OTHER COMMENTS:
##      Any special comments
##
########################################################################
