import random
import time

# mainNumerot = [1, 2, 3, 4, 5]
# additionalNumerot = [1, 2, 3]
# mainUserNumerot = [9, 8, 7, 6, 5]
# additionalUserNumerot = [3, 2, 1]
mainNumerot = []
additionalNumerot = []
mainUserNumerot = []
additionalUserNumerot = []
lengthOfMain = 7
lengthOfadditional = 3

def askUser(array, num1, num2):
    x = int(input("Input number "+str(num1+1)+" of "+str(num2)+" between 1-39: "))
    if (0 <= x <= 40) & (not x in array): array.append(x)
    else:
        print("You do a wrong input. Please try again.") 
        askUser(array, num1, num2)

print("\n")
for i in range(lengthOfMain): askUser(mainUserNumerot, i, lengthOfMain)
print("\n")
for i in range(lengthOfadditional): askUser(additionalUserNumerot, i, lengthOfadditional)

mainUserNumerot.sort()
additionalUserNumerot.sort()

print("\n\nSo, your Main numbers are: ")
print(*mainUserNumerot)
print("\nAnd, your Additional numbers are: ")
print(*additionalUserNumerot)

def generateLotto(array):
    x = random.randrange(1, 40, 1)
    if not x in array: array.append(x)
    else: generateLotto(array)

for i in range (lengthOfMain): generateLotto(mainNumerot)
for i in range (lengthOfadditional): generateLotto(additionalNumerot)

mainNumerot.sort()
additionalNumerot.sort()

def compareLists(firstList, secondList):
    tempList = []
    for x in firstList:
        if x in secondList:
            tempList.append(x)
    return tempList
    # return [x for x in firstList if x in secondList]

mainSame = compareLists(mainUserNumerot, mainNumerot)
addittionalSame = compareLists(additionalUserNumerot, additionalNumerot)

print("\nLet's see, what number are the same...")
time.sleep(2)
if len(mainSame) > 0:
    if len(addittionalSame) > 0:
        print("\nIn a Main here the same are:")
        print(*mainSame)
        print("\nIn a Additional here the same are:")
        print(*addittionalSame)
    else:
        print("\nIn a Main here the same are:")
        print(*mainSame)
else: print("Sorry, there is not the same numbers")

if len(mainSame) == 7:
    print("You have 1th place")
elif (len(mainSame) == 7) & (len(addittionalSame) > 0):
    print("You have 2th place")
elif len(mainSame) == 6:
    print("You have 3th place")
elif len(mainSame) == 5:
    print("You have 4th place")
elif len(mainSame) == 4:
    print("You have 5th place")
else: print("Sorry, but you win nothing :( But You can try one more time ;)")

print("\nMain numbers was:")
print(*mainNumerot)
print("\nAdditional numbers was:")
print(*additionalNumerot)