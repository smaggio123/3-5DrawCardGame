import random
from Player import Player
from Deck import Deck
from Card import Card

print("first to three wins")
d=Deck()
d.shuffle()
p1 = Player()
comp = Player()


hand1 = [d.deck[0], d.deck[1], d.deck[2], d.deck[3], d.deck[4]]
hand2 = [d.deck[5], d.deck[6], d.deck[7], d.deck[8], d.deck[9]]

del d.deck[0:10]

p1.hand=hand1
comp.hand=hand2

p1Wins=0
compWins=0

def convertToNum(str):
    if str[0:3] == 'Ace':
        return 14
    elif str[0:4] == 'King':
        return 13
    elif str[0:5] == 'Queen':
        return 12
    elif str[0:4] == 'Jack':
        return 11
    elif str[0:2] == '10':
        return 10
    else:
        return int(str[0])
keepPlaying=True
while keepPlaying:
    print("your hand")
    print(p1.hand)
#    print("computer hand")
 #   print(comp.hand)

    p1PickedCard=Card("","")

    valid=False
    while not valid:
        playerPick=int(input("pick a card: 1-5\n"))
        if 5 >= playerPick >= 1:
            p1PickedCard=p1.hand[playerPick-1]
            del p1.hand[playerPick-1]
            valid=True
        else:
            print("Number not in range")

    value = comp.pickCard()
    compPickedCard = Card("","")
    compPickedCard = comp.hand[value]
    del comp.hand[value]

    print("your pick")
    print(p1PickedCard)
    print("computer picked")
    print(compPickedCard)

    playerOneNum = convertToNum(p1PickedCard)
    computerNumber = convertToNum(compPickedCard)
    if playerOneNum > computerNumber:
        p1Wins += 1
        print("You won a round")
    if playerOneNum < computerNumber:
        compWins += 1
        print("You lost the round")
    if playerOneNum == computerNumber:
        print("tie")

    p1.hand.append(d.deck[0])
    del d.deck[0]
    comp.hand.append(d.deck[0])
    del d.deck[0]

    print("Player1: "+str(p1Wins)+" computer: "+ str(compWins))
    if p1Wins >= 3:
        keepPlaying = False
        print("you win")
    elif compWins >= 3:
        keepPlaying = False
        print("You lose")

    #ans1=input("Would you like to play again?")
    #if ans1=="n":
        #keepPlaying=False;
