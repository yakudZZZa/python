word = "*"

print ("Using for-loop")
for i in reversed(range(7)): print(word*i)

print ("Using while-loop")
count = 7
while (count > 0): 
    print(word*count)
    count -= 1
