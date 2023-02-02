word = "*"
width = int(input("Input rectagnle width: "))
height = int(input("Input rectagnle height: "))
result = word*width

print ("Using for-loop")
for i in range(height): print(result)

print ("\nUsing while-loop")
while height > 0: 
    print(result)
    height -= 1