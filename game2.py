import random as r
import pandas as p
import numpy as np
import plotly as pl
import matplotlib.pyplot as plt

Results = []  # if winOrLoss[i] is negative, game lost, if positive, game won

def play_game2_once(slotBettedOn):
    resultOfSpin = r.randint(0, 36)
    if resultOfSpin == slotBettedOn:
        return 35
    else:
        return -1


# playing game 10,000 times
for i in range(10000):
    slotBettedOn = r.randint(0, 36)
    currentResult = play_game2_once(slotBettedOn)
    Results.append(currentResult)


# C1 - expected winnings per game
winslossesArr = []
wins = 0
losses = 0
totalWinnings = 0
for i in Results:
    currentResult = i
    if currentResult > 0:
        wins += 1
        winslossesArr.append(1)
    elif currentResult < 0:
        losses += 1
        winslossesArr.append(0)
    totalWinnings += currentResult

print("wins = " + str(wins))
print("losses = " + str(losses))
print("Total Winnings = " + str(totalWinnings))
expectedWinnings = totalWinnings/10000
#A)
print("TASKS:\nA)\nCrit1) Expected winnings per game = " + str(expectedWinnings))
winsProportion = wins/10000
print("Crit2) Proportion of wins = " + str(winsProportion))
print("Crit3) Expected playing time per game = 1 bet made")
print("Crit4) Maximum amount you can lose = 1$")
print("Crit5) Maximum amount you can win = 35$")

#B)
realExpectedWinnings = -0.027
realWinsProportion = 0.027027
print("\nB) P E R C E N T A G E   E R R O R")
print("Exact answers :\nCrit1) Expected winnings per game = -$0.027\nCrit2) Proportion of games you win =" + str(realWinsProportion))
winsPercentageError = abs(((realExpectedWinnings - expectedWinnings)/realExpectedWinnings)*100)
print("\nPercentage error :\nCrit1) Expected winnings per game = " + str(winsPercentageError) + "%")
proportionPercentageError = abs(((realWinsProportion - winsProportion)/realWinsProportion)*100)
print("Crit2) proportion of games you win = " + str(proportionPercentageError) + "%")

#C)

print("\nC) P L O T   R U N N I N G   A V E R A G E  +  R U N N I N G   V A R I A N C E\n")

#winnings crit 1
runningWinningsAverage = []
runningWinningsVariance = []
repetitions = []
for i in range(2 , 10000):
    repetitions.append(i)
    totalAverage = 0.0
    totalVariance = 0.0
    length = 0
    for j in range(i):
        totalAverage += Results[j]
        length +=1
    totalAverage/= length
    runningWinningsAverage.append(totalAverage)
    length = 0
    for j in range(i):
        totalVariance += (Results[j] - totalAverage) ** 2
        length += 1
    totalVariance /= (length -1)
    runningWinningsVariance.append(totalVariance)

plt.plot(repetitions, runningWinningsAverage, label="Running average of winnings")
plt.plot(repetitions, runningWinningsVariance, label="Running variance of winnings")
plt.xlabel("Repetitions of game")
plt.ylabel("Values")
plt.title("Running average and variance of winnings!")
plt.legend()
plt.show()

#proportion of games won - crit2
PropWinsRAarray = []
PropWinsVarArray = []
repetitions = []
for i in range(2, 10000):
    repetitions.append(i)
    totalAverage = 0.0
    totalVariance = 0.0
    length = 0
    for j in range(i):
        totalAverage += winslossesArr[j]
        length += 1
    totalAverage /= length
    PropWinsRAarray.append(totalAverage)
    length = 0
    for j in range(i):
        totalVariance += (winslossesArr[j] - totalAverage) ** 2
        length +=1
    totalVariance /= (length - 1)
    PropWinsVarArray.append(totalVariance)

plt.plot(repetitions, PropWinsRAarray, label="Running average of winning proportions")
plt.plot(repetitions, PropWinsVarArray, label="Running variance of of winning proportions")
plt.xlabel("Repetitions of game")
plt.ylabel("Values")
plt.title("Running average and variance of winning proportions")
plt.legend()
plt.show()


# Variance for A)
print("D) V A R I A N C E   F O R   P A R T   A)")

#variance of expected winnings per game
VarianceofWinnings = []
VarianceOfProportionOfWins = []

for i in range(10):
    Results = []
    for x in range(10000):
        randomNum = r.randint(0, 36)
        currentResult = play_game2_once(randomNum)
        Results.append(currentResult)
    Winnings = 0
    Losses = 0
    wins = 0
    for y in Results:
        if y > 0:
            Winnings += y
            wins += 1
        if y < 0:
            Losses += y

    VarianceOfProportionOfWins.append(wins/10000)
    VarianceofWinnings.append(Winnings/10000)

varianceWinningsPartD = (np.var(VarianceofWinnings, ddof=1))
varianceProportionsPartD = (np.var(VarianceOfProportionOfWins, ddof=1))
print("Crit1) Variance of 10 expected winnings = " + str(varianceWinningsPartD))
print("Crit2) Variance of proportion of winning in 10 simulations = " + str(varianceProportionsPartD))
print("Playing time, maximum amount you can lose and maximum amount you can win doesn't change thus Variance = 0")
















