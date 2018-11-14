import random

rounds = 1
BeatRound = 1
money = 15
MostMoney = money
while money > 0:
    if MostMoney < money:
        MostMoney = money
        BestRound = Rounds
     Rounds =(rounds + 1)
    print("you have %d dollars" % money)
    FirstDice = random.randint(0, 4)
    SecondDice = random.randint(0, 6)
    print("Dice One is %d " % FirstDice)
    print("And Dice Two is %d " % SecondDice)
    Adding = (FirstDice + SecondDice)
    if Adding is 7:
        print("Congratulations!You are so lucky!")
        money = (money + 5)
        print(money)
    else:
        print("You lost the bet")
        money - (money - 1)
        print(money)
print("The Number of Rounds to run out of money %d" % Rounds)
print("You Should HAVE Stopped at  Round %d When you had %d Dollars"%  BestRound MostMoney)
