lowNumber = 1
highNumber = 10

userInput:int = int(input ("Please input a number 1-10\n"))
if (lowNumber <= userInput <= highNumber):
    for x in range (10): print (userInput + x * userInput)
else: print ("This is not a number in 1-10")

userInput2:int = int(input ("Please input a number 1-10\n"))
if (lowNumber <= userInput2 <= highNumber):
    for x in reversed (range (10)): print (userInput2 + x * userInput2)
else: print ("This is not a number in 1-10")