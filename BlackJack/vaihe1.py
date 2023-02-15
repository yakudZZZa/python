import random
import time

# userCardsString = [3, "A", "A", "K", 6]
userCardsString = []
userCounterList = []
userScore: int = 0
dealerCardsString = []
dealerCounterList = []
dealerScore: int = 0
userScoreWins = 0
dealerScoreWins = 0
questionToAddCard = "Do you want to add card (y/n)?: "
questionToReplay = "Do you want to play one nore time (y/n)?: "
positiveAnswers = ["y", "yes"]
negativeAnswers = ["n", "no"]

cards = {'A':1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10, 'J':11, 'Q':12, 'K':13}
# suitsDeck = ["clubs", "diamonds", "hearts", "spades"]
suitsDeck = ["\u2660", "\u2663", "\u2665", "\u2666"]
cardsDeck = [2,3,4,5,6,7,8,9,10,"J","Q","K","A"]
# suitsDeck = list(map(str.upper, suitsDeck))
random.shuffle(suitsDeck)
for i in range(10): random.shuffle(cardsDeck)

def getRandomCard(inputSuits: list, inputCards: list, outputCardsString: list, outputCounterList: list):
    choisedSuite = str(random.choice(inputSuits))
    choisedCard = str(random.choice(inputCards))
    # outputCardsString.append(choisedSuite + " " + choisedCard)
    outputCardsString.append(choisedCard + " " + choisedSuite)
    outputCounterList.append(choisedCard)

def getGoodString(fromList: list):
    x = ""
    for i in fromList:
        x += i + ', '
    return x[:-2]


def countNominal(in_list):
    tempCount = 0
    bigAceWas = False
    for number in in_list:
        if number == "J" or number == "Q" or number == "K":
            if (tempCount + 10 > 21) and (bigAceWas) :
                tempCount -= 10
                bigAceWas = False
            tempCount += 10
        elif number == "A":
            if (tempCount + 11 > 21) and (bigAceWas) :
                tempCount -= 10
                bigAceWas = False
                tempCount += 1
            elif (tempCount + 11 > 21) and (not bigAceWas):
                tempCount += 1
            else: 
                tempCount += 11
                bigAceWas = True
        else: 
            if (tempCount + int(number) > 21) and (bigAceWas) :
                tempCount -= 10
                bigAceWas = False
            tempCount += int(number)
    return tempCount

def dealerPlay():
    dealerScore = 0
    print("\nWell now it's the Dealer's turn")
    while dealerScore < 17:
        if dealerScore > 0: print("\nDealer get one more card")
        else: print("\nDealer get one card")
        getRandomCard(suitsDeck, cardsDeck, dealerCardsString, dealerCounterList)
        dealerScore = countNominal(dealerCounterList)
        time.sleep(2)
        print("Dealer's cards is:", getGoodString(dealerCardsString))
        print("Dealer's score is:", dealerScore)
    if dealerScore > 21:
        print("\nDealer have " + str(dealerScore) + " points and it's more than 21. Dealer is lost.")
    else:
        print("\nOk, Dealer have a good cards. Dealer's Score is " + str(dealerScore) + ". Let's check who is win!")
    return dealerScore

def userPlay():
    userScore = 0
    desireToContinue = True
    while desireToContinue and userScore <= 21:
        if userScore > 0:
            while True:
                userAnswer = input(questionToAddCard).lower()
                if userAnswer in positiveAnswers: 
                    desireToContinue = True
                    getRandomCard(suitsDeck, cardsDeck, userCardsString, userCounterList)
                    userScore = countNominal(userCounterList)
                    print("User's cards is:", getGoodString(userCardsString))
                    print("User's score is:", userScore, "\n")
                    break
                if userAnswer in negativeAnswers: 
                    desireToContinue = False
                    break
        else:
            print("Here your first card")
            getRandomCard(suitsDeck, cardsDeck, userCardsString, userCounterList)
            userScore = countNominal(userCounterList)
            print("User's cards is:", getGoodString(userCardsString))
            print("User's score is", userScore, "\n")
    if userScore > 21:
        print("User have " + str(userScore) + " points and it's more than 21. You lost.")
    else:
        print("\nOk, User have a good cards. User's Score is " + str(userScore) + ". Let's check what the Dealer has!\n")
    return userScore

while True:
    print("\nWell, let's play!\n")
    userScore = userPlay()
    dealerScore = dealerPlay()
    print("\n")

    if userScore > 21 and dealerScore > 21:
        print("Nobody won :(")
    elif userScore > dealerScore and userScore > 21:
        dealerScoreWins += 1
        print("The Dealer has won!")
    elif userScore < dealerScore and dealerScore > 21:
        userScoreWins += 1
        print("The User has won!")
    elif userScore > dealerScore:
        userScoreWins += 1
        print("The User has won!")
    elif userScore < dealerScore:
        dealerScoreWins += 1
        print("The Dealer has won!")
    elif userScore == dealerScore:
        print("This game has parity")

    print("\n")
    userAnswer = input(questionToReplay).lower()
    if userAnswer in positiveAnswers: 
        userCardsString = []
        userCounterList = []
        userScore: int = 0
        dealerCardsString = []
        dealerCounterList = []
        dealerScore: int = 0
    if userAnswer in negativeAnswers:
        print("\n\n\nWell played! User won", userScoreWins, "times and Dealer won", dealerScoreWins, "times.\n")
        break