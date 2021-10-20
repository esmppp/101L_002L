##Ethan Miller
##esmppp@umsystem.edu
##CS 101 
##Program 6
##
##PROBLEM: Do Caesar Encryption/Decryption
##  
##Functions needed: 
##  Encrypt(string_text, int_key): Takes a string and integer key, returns 
##  the encryption of the string using that key. Note that for Caesar encryption, 
##  an encryption with key k (k in 1 - 25) is decrypted by doing the same process 
##  with key 26-k. Returns encrypted string using specified key. 
##  
##  Decrypt(string_text, int_key): Decrypts key by calling Encrypt with key 
##    26-int_key and returning the result. Done this way to make for a cleaner
##    breakdown of the problem. Returns decrypted string using specified key. 
##    
##  Get_input(): Interacts with user, gets user choice of '1','2','Q' and returns that 
##  value. If user enters anything else, prints brief error message and tries again. 
##  
##  Print_menu(): Prints menu. No user interaction. 
  
################################ 
import string
def stageChecker():
  print("MAIN MENU")
  staged = input("1) Encode a string\n2) Decode a string\nQ) Quit\nEnter your selection ==> ")
  while staged not in '12Qq':
    staged = input("ERROR TRY AGAIN\n1) Encode a string\n2) Decode a string\nQ) Quit\nEnter your selection ==> ")
  return staged

#This is the actual Caeser Cipher. It uses nested if-elif-else statements to check if the character is capital or lowercase, and if it goes beyond A-Z and needs to loop around
def Encrypt(string, givenKey):
    newMessage = ''
    for i in string:
      if i not in letters:
        newMessage += i
      elif i in caps:
        if((ord(i)+key) >90):
          newMessage += chr(ord(i)+key-26)
        elif((ord(i)+key) <65):
          newMessage += chr(ord(i)+key+26)
        else:
          newMessage += chr(ord(i)+key)
      elif i in lows:
        if((ord(i)+key) >122):
          newMessage += chr(ord(i)+key-26)
        elif((ord(i)+key) <97):
          newMessage += chr(ord(i)+key+26)
        else:
          newMessage += chr(ord(i)+key)
    return newMessage.upper()

def Decrypt(string, givenKey):
    newMessage = ''
    for i in string:
      if i not in letters:
        newMessage += i
      elif i in caps:
        if((ord(i)+key) >90):
          newMessage += chr(ord(i)+key-26)
        elif((ord(i)+key) <65):
          newMessage += chr(ord(i)+key+26)
        else:
          newMessage += chr(ord(i)+key)
      elif i in lows:
        if((ord(i)+key) >122):
          newMessage += chr(ord(i)+key-26)
        elif((ord(i)+key) <97):
          newMessage += chr(ord(i)+key+26)
        else:
          newMessage += chr(ord(i)+key)
    return newMessage.upper()


#This uses the function to update the sentinel variable for the while loop
stage = stageChecker()
#These 3 lists are set up by the following for loops, and they're used to check if the inputted string's character is a letter (and therefore gets changed), or if it's a non-letter input, like a number or !.
letters = []
caps = []
lows = []
for i in range(ord('A'),ord('Z')+1):
  caps.append(chr(i))
  letters.append(chr(i))
for i in range(ord('a'),ord('z')+1):
  lows.append(chr(i))
  letters.append(chr(i))


while stage.upper() != "Q":
  #First option: Coding a statement
  if(stage.upper() == "1"):
    print()
    message = input("Enter (brief) text to encrypt: ")
    key = int(input('Enter the number to shift letters by: '))
    codedMessage = Encrypt(message,key)
    print("Encrypted:", codedMessage)
    print()
  #Second option: Decoding a statement
  if(stage.upper() == "2"):
    print()
    codedMessage = input("Enter (brief) text to decrypt: ")
    key = int(input('Enter the number to shift letters by: '))
    #Reverses the key to decode
    key = -key
    decodedMessage = Decrypt(codedMessage,key)
    print("Decrypted:", decodedMessage)
    print()
  #Checks if user wants to code/decode again
  stage = stageChecker()
