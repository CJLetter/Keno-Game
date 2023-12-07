def main():
    # Define Lists
    prize = False
    picklist = []
    winninglist = []

    printHeader()
    picklist = getPicks(picklist)
    input("Press the [Enter] key to generate the winning Keno numbers.")
    winninglist = generateKeno(winninglist)
    matchlist = checkMatches(picklist, winninglist)

    print(f"\nYour picks are: ")
    print(f" {picklist}")
    print(f"\nThe winning numbers are: ")
    print(f" {winninglist}")

    print(f"\nYou matched: ")
    print(f" {matchlist}")

    if len(matchlist) >= 10:
        print(f"\nYou matched {len(matchlist)} of 20 numbers. You won $250,000.")
    elif len(matchlist) == 9:
        print(f"\nYou matched {len(matchlist)} of 20 numbers. You won $2,500.")
    elif len(matchlist) == 8:
        print(f"\nYou matched {len(matchlist)} of 20 numbers. You won $250.")
    elif len(matchlist) == 7:
        print(f"\nYou matched {len(matchlist)} of 20 numbers. You won $25.")
    elif len(matchlist) == 6:
        print(f"\nYou matched {len(matchlist)} of 20 numbers. You won $7.")
    elif len(matchlist) == 5:
        print(f"\nYou matched {len(matchlist)} of 20 numbers. You won $1.")
    else:
        print(f"\nYou matched {len(matchlist)} of 20 numbers. You did not win a prize.")


def printHeader():
    print("Keno Lottery Game\n")

def getPicks(picklist):
    picksdone = False
    counter = 1
    while not picksdone:
        try:
            if len(picklist) < 10:
                pick = int(input(f'Enter pick #{counter}: '))
                if pick in picklist:
                    print(f'{pick} has already been picked. Try again')
                elif pick < 1 or pick > 80:
                    print("Value out of range. Try again")
                else:
                    picklist.append(pick)
                    counter+=1
            else:
                picksdone = True
        except:
            print('Invalid data. Try again.')
    return picklist

def generateKeno(winninglist):
    listdone = False
    while not listdone:
        if len(winninglist) <20:
            winNumb = random.randint(1, 80)
            if winNumb in winninglist:
                winninglist.remove(winNumb)
            winninglist.append(winNumb)
        else:
            listdone = True
    return winninglist

def checkMatches(picklist, winninglist):
    matchlist = []
    templist = []
    i = 0

    templist = picklist + winninglist
    while i < len(templist):
        if templist.count(i) > 1:
            matchlist.append(i)
        i += 1
    return matchlist

if __name__ == '__main__':
    import random
    main()
