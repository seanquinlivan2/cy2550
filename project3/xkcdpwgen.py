import sys 
import random
#import urllib2
from pathlib import Path
f_path = Path("words.txt")

f = open("words.txt")
list = f.read().split()
arguments = sys.argv
wordCount = 4
caps = 0
if (arguments.count("-w")):
    wordCount = arguments[arguments.count("-w") + 1]
numbers = 0
list2 = []
symbols = 0
los= ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "+", "-","~"]
if (arguments.count("-c") > 0) :
    caps = arguments[arguments.index("-c") + 1]
if (arguments.count("-n")):
    numbers = arguments[arguments.index("-n") + 1]
if (arguments.count("-s")):
    symbols = arguments[arguments.index("-s") + 1]
if (arguments.count("-h")) :
    print("Generate a secure password using XKCD method: \n Options: \n -n # how many numbers you want in password. \n -c # how many caps you want in password.")
    print("-s # how many symbols you want in password.\n -w # how many words you want in password.\n")

password = ""

if caps > wordCount:
    caps = wordCount

passwordList = random.sample(list,int(wordCount))
for i in range(0,int(caps)) :
    i = 1
    while i :
        index = random.randint(0, len(passwordList) - 1)
        if (list2.count(index) == 0) :
            i = 0
            list2.append(index)
    oneW = passwordList[index]
    passwordList[index] = oneW.capitalize()

for i in range(0, int(numbers)):
    spot = random.randint(0, len(passwordList))
    passwordList.insert(spot, random.randint(0,9))

for i in range(0, int(symbols)):
    spot = random.randint(0, len(passwordList))
    passwordList.insert(spot, random.choice(los))

for i in range(0,len(passwordList)):
     s = passwordList[i]
     password = password + str(s)



print(password)
