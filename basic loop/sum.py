number = int(input("Input a number for sum: "))

print ("Calculate sum by using for-loop: ")
tempNumber = number
for i in range(1, number): tempNumber += i
print (tempNumber)

print ("Calculate sum by using while-loop: ")
tempNumber = number
while number > 1:
    number -= 1
    tempNumber += number
print (tempNumber)