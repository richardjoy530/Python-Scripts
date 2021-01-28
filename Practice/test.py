n = int(input)
astr = input().split()

firstHalf = astr[0:int(n/2)]
secondHalf = astr[int(n/2):]

firstChars = []
lastChars = []

for i in firstHalf:
    firstChars.append(i[0])

for i in secondHalf:
    lastChars.append(i[-1]) 

charList = firstChars+lastChars

myNumber = ''

for i in charList:
    myNumber = myNumber+i

myNumber = int(myNumber)

if myNumber%11==0:
    print("OUI")
else:
    print("NON")