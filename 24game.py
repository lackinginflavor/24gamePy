import random

playNumbers = []
for x in range(4):
    playNumbers.append(random.randint(1,9) + 0.0)

print "The object of this game is to take the below numbers and make them equal 24."
print playNumbers
print "You can use any +, -, *, / and ()"
userInput = raw_input('Please enter your expression now:')

userList = []
for s in userInput:
    userList.append(s)

print userList

for r in userList:
    if r == ' ':
        userList.remove(' ') #trying to remove spaces
    elif r.isdigit():
        r = float(r) #trying to  convert '#s' to floats
    elif r != '*' or r != '/' or r != '+' or r != '-' or r != '(' or r != ')':
        userList.remove(r)
        print "You had an invalid entry"

print userList
