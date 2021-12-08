#game-1 betting on red

from random import choice
import matplotlib.pyplot as plt

winnings = []
playTime = []
arrayOfWinnings = []
arrayOfPropWinnings = []
arrayOfPlayTime = []

repetitions = 10000
gamesWon = []
winReturn = 1
lossReturn = -1

sequence = [i for i in range(37)]

for x in range(10):
    totalBets = 0
    winning = 0
    wins = 0
    for y in range(repetitions):
        pocket = choice(sequence)
        if pocket % 2 == 1:
            winning += winReturn
            wins += 1
            winnings.append(winReturn)
            gamesWon.append(winReturn)
        else:
            winnings.append(lossReturn)
            gamesWon.append(0)
            winning += lossReturn
        totalBets += 1
        playTime.append(1)
    arrayOfWinnings.append(winning/totalBets)
    arrayOfPropWinnings.append(wins/totalBets)
    arrayOfPlayTime.append(totalBets/repetitions)


#Task A
print("Task A")

#expected winnings
expWinnings = winning / totalBets
print("Expected winnings: " + str(expWinnings))

#proportion of games won
proportionWon = wins / totalBets
print("Proportion of games won: " + str(proportionWon))

#expected playing time per game
playingTime = totalBets / repetitions
print("Playing time: " + str(playingTime))

#maximum amount you can lose
print("Max loss: $" + str(abs(lossReturn)))

#maximum amount you can win
print("Max win: $" + str(winReturn))


#Task B
print("\nTask B")

exactExpWinnings = (18 / 37) - (19 / 37)
exactProportionWon = (18 / 37)

print("Exact answers for c1 and c2 :\nexpected winnings per game = {:.3f}".format(exactExpWinnings) + "\nproportion of games you win = {:.3f}".format(exactProportionWon))

expWinningsPercentageError = abs(((expWinnings - exactExpWinnings) / exactExpWinnings) * 100)
print("\nPercentage error :\nExpected winnings per game = {:.3f}".format(expWinningsPercentageError) + "%")

proportionPercentageError = abs(((proportionWon - exactProportionWon) / exactProportionWon) * 100)
print("Proportion of games you win = {:.3f}".format(proportionPercentageError) + "%")


# #Task C
runningAverage =[]
runningVariance = []
reps = []

for i in range(2, repetitions):
    reps.append(i)
    totalAverage = 0.0
    totalVariance = 0.0
    length = 0
    for j in range(i):
        totalAverage += winnings[j]
        length += 1
    totalAverage /= length
    runningAverage.append(totalAverage)
    length = 0
    for j in range(i):
        totalVariance += (winnings[j] - totalAverage) ** 2
        length += 1
    totalVariance /= length - 1
    runningVariance.append(totalVariance)

plt.plot(reps, runningAverage, label="Running average of winnings")
plt.plot(reps, runningVariance, label="Running variance of winnings")
plt.xlabel("Repetitions of game")
plt.ylabel("Values")
plt.title("Running average and variance of winnings!")
plt.legend()
plt.show()

runningAverage =[]
runningVariance = []

for i in range(2, repetitions):
    totalAverage = 0
    totalVariance = 0
    length = 0
    for j in range(i):
        totalAverage += gamesWon[j]
        length += 1
    totalAverage /= length
    runningAverage.append(totalAverage)
    length = 0
    for j in range(i):
        totalVariance += (gamesWon[j] - totalAverage) ** 2
        length += 1
    totalVariance /= length - 1
    runningVariance.append(totalVariance)

plt.plot(reps, runningAverage, label="Running average of wins")
plt.plot(reps, runningVariance, label="Running variance of wins")
plt.xlabel("Repetitions of game")
plt.ylabel("Values")
plt.title("Running average and variance of wins!")
plt.legend()
plt.show()

#Task D
print("\nTask D")

total = 0
for i in arrayOfWinnings:
    total += i
expectedTotalWins = total/10
total = 0
for i in arrayOfWinnings:
    total += (i - expectedTotalWins) ** 2
winningsVariance = total / 9
print("Expected winnings variance: " + str(winningsVariance))

total = 0
for i in arrayOfPlayTime:
    total += i
expectedPlayingTime = total/10
total = 0
for i in arrayOfPlayTime:
    total += (i - expectedPlayingTime) ** 2
playingTimeVariance = total/9
print("Expected playing time variance per game: " + str(playingTimeVariance))

for i in arrayOfPropWinnings:
    total += i
expectedPropOfGamesWon = total/10
total = 0
for i in arrayOfPropWinnings:
    total += (i - expectedPropOfGamesWon) ** 2
propOfGamesWonVariance = total / 9
print("Proportion of games won variance : " + str(propOfGamesWonVariance))



