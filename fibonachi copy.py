choise = int(input("Saadaksesi Fibonacci-sekvenssin, syötä haluamasi määrä arvoja sekvenssiin (sen on oltava nollaa suurempi kokonaisluku)"))
fibArray = [0, 1]
def fibonacci (n):
    if n < 1: print ("Saadaksesi Fibonacci-sekvenssin, syötä haluamasi määrä arvoja sekvenssiin (sen on oltava nollaa suurempi kokonaisluku)")
    elif n == 1: print (fibArray[0])
    else: 
        for i in range (2, n): fibArray.append(fibArray[i-1] + fibArray[i-2])
        print (*fibArray)

print("Te valitsitte numero: " + str(choise))
fibonacci(choise)
