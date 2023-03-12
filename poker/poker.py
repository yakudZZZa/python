import random
import time

hand: list[int, str] = []
questionToReplay = "Do you want to play one nore time (y/n)?: "
positiveAnswers = ["y", "yes"]
negativeAnswers = ["n", "no"]

suitsDeck = ["\u2660", "\u2663", "\u2665", "\u2666"]
cardsDeck = [i for i in range(2, 15)]

def convertCardValueToString(inputInt: int) -> str:
    match inputInt:
        case 11: return 'J'
        case 12: return 'Q'
        case 13: return 'K'
        case 14: return 'A'
        case _: return str(inputInt)

def getBeautifulString(fromList) -> str:
    return ', '.join([convertCardValueToString(value[0]) + ' ' + value[1] for value in fromList])

def getShuffledList(list: list) -> list:
    tempCopy = list.copy()
    random.shuffle(tempCopy)
    return tempCopy

def getRandomCard(suitsDeck: list, cardsDeck: list, hand: list):
    for i in range(5):
        while len(hand) == i:
            randomSuite = random.choice(getShuffledList(suitsDeck))
            randomCard = random.choice(getShuffledList(cardsDeck))
            if not ((randomCard, randomSuite)) in hand:
                hand.append((randomCard, randomSuite))
    hand.sort()

def fullCheck(hand: list, manyTimes: bool = False):
    if not hand: return print('Hand is empty')
    valuesInt = sorted([card[0] for card in hand])
    suits = [card[1] for card in hand]
    value_counts: dict[int, int] = { value: valuesInt.count(value) for value in set(valuesInt) }

    def checkPara() -> bool: return 2 in value_counts.values()
    def checkTwo() -> bool: return 2 == sum(value == 2 for value in value_counts.values())
    def checkThree() -> bool: return 3 in value_counts.values()
    def checkFour() -> bool: return 4 in value_counts.values()
    def checkFullHouse() -> bool: return 3 in value_counts.values() and 2 in value_counts.values()
    def checkFlash() -> bool: return len(set(suits)) == 1
    def ckeckStreet() -> bool: return valuesInt == [14, 2, 3, 4, 5] or all(valuesInt[i] + 1 == valuesInt[i + 1] for i in range(len(valuesInt) - 1))
    def ckeckRoyalFlush() -> bool: return valuesInt == [10, 11, 12, 13, 14] and checkFlash()
    
    if manyTimes:
        if ckeckRoyalFlush(): return 'Royal Flush'
        elif ckeckStreet() and checkFlash(): return 'Straight Flush'
        elif checkFour(): return 'Four of kind'
        elif checkFullHouse(): return 'Full House'
        elif checkFlash(): return 'Flush'
        elif ckeckStreet(): return 'Straight'
        elif checkThree(): return
        elif checkTwo(): return
        elif checkPara(): return
        else: return
    else:
        if ckeckRoyalFlush(): print('You have a Royal Flush!\n')
        elif ckeckStreet() and checkFlash(): print('You have a Straight Flush!\n')
        elif checkFour(): print('You have a Four of kind!\n')
        elif checkFullHouse(): print('You have a Full House!\n')
        elif checkFlash(): print('You have a Flush!\n')
        elif ckeckStreet(): print('You have a Straight!\n')
        elif checkThree(): print('You have a Three of kind!\n')
        elif checkTwo(): print('You have a Two Pair!\n')
        elif checkPara(): print('You have a One Pair!\n')
        else: print('Unfortunately, you have nothing\n')

def test():
    hand.append((11, '♥'))
    hand.append((9, '♥'))
    hand.append((9, '♥'))
    hand.append((11, '♥'))
    hand.append((11, '♦'))
    hand.sort()
    print('\n')
    print(getBeautifulString(hand))
    fullCheck(hand)

def pokerGame(times = 0, withLog = False):
    global hand
    turns = 0
    stat: list[str] = []
    print("\nWell, let's play!\n")

    if times == 0:
        while True:
            getRandomCard(suitsDeck, cardsDeck, hand)
            print(getBeautifulString(hand))
            result = fullCheck(hand)
            userAnswer = input(questionToReplay).lower()
            
            if userAnswer in positiveAnswers: 
                print('\n')
                hand = []
            elif userAnswer in negativeAnswers:
                break
    else: 
        while turns < times:
            turns += 1
            getRandomCard(suitsDeck, cardsDeck, hand)
            if withLog:
                print("Turn:", turns)
                print(getBeautifulString(hand), '\n')
            result = fullCheck(hand, True)
            if result:
                stat.append(result)
            hand = []
            if turns == times:
                print('Games was:', times, '\n')
                stringStat = ''.join("{0} was: {1}\n".format(k, v) for k, v in sorted({ value: stat.count(value) for value in set(stat) }.items(), key=lambda value:value[1]))
                if stringStat: print (stringStat)
                else: print('There was no good combination\n')

# test()
pokerGame()
# pokerGame(10)
# pokerGame(10, True)