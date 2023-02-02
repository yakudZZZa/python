word = "*"
width = 10
height = 4
result = word*width

print ("Using for-loop")
for i in range(height): print(result)

print ("\nUsing while-loop")
while height > 0: 
    print(result)
    height -= 1