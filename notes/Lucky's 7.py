import random

Rounds = 1
BeatRound = 1
money = 15
MostMoney = money
while money > 0:
    if MostMoney < money:
        MostMoney = money
        Bestround = Rounds
        Rounds = (round + 1)
    print("you have %d dollars" % money)
    FirstDice = random.randint(1, 4)
    SecondDice = random.randint(1, 6)
    print("Dice One is %d " % FirstDice)
    print("And Dice Two is %d " % SecondDice)
    Adding = (FirstDice + SecondDice)
    if Adding is 7:
        print("Congratulations!You are so lucky!")
        money = (money + 5)
        print(money)
    else:
        print("You lost the bet")
        money = (money - 1)
        print(money)
