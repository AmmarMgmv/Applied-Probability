import numpy as np
import matplotlib.pyplot as plt
import random

running = True
reps = 10000
expectedWinsArr = []
expectedPlayingTimeArr = []
expectedPropOfGamesWonArr = []
winningsArr = []
gamesWonArr = []
maxWon = 0
maxLost = 0

for j in range(10):
    totalWinnings = 0
    totalPlayingTime = 0
    won = 0
    winnings = 0
    playingTime = 0
    for i in range(reps):
        start = [1, 2, 3, 4]
        winnings = 0
        playingTime = 0

        while running:
            if len(start) == 1:
                bet = start[0]
                if bet == 100:
                    break
                playingTime += 1
                value = random.randint(0, 36)
                if 18 >= value >= 1:
                    winnings += bet
                    start = np.delete(start, 0)
                else:
                    winnings -= bet
                    start = np.insert(start, len(start), bet)
            else:
                bet = start[0] + start[-1]
                if bet == 100:
                    break
                playingTime += 1
                value = random.randint(0, 36)
                if 18 >= value >= 1:
                    winnings += bet
                    start = np.delete(start, 0)
                    start = np.delete(start, -1)
                else:
                    winnings -= bet
                    start = np.insert(start, len(start), bet)

            if len(start) == 0:
                break
        totalWinnings += winnings
        totalPlayingTime += playingTime
        if maxWon < winnings:
            maxWon = winnings
        if maxLost > winnings:
            maxLost = winnings
        if winnings > 0:
            won += 1
        if i != 0:
            winningsArr.append(winnings)
            if winnings > 0:
                gamesWonArr.append(1)
            else:
                gamesWonArr.append(0)
    expectedWinsArr.append(totalWinnings / reps)
    expectedPropOfGamesWonArr.append(won / reps)
    expectedPlayingTimeArr.append(totalPlayingTime / reps)

expectedWins = 0
playingTime = 0
propOfGamesWon = 0

total = 0
for i in expectedWinsArr:
    expectedWins = i
    total += i
expectedTotalWins = total/10

print("Expected winnings per game: " + str(expectedWins))
total = 0
for i in expectedWinsArr:
    total += (i - expectedTotalWins) ** 2
winningsVariance = total / 9

total = 0
for i in expectedPlayingTimeArr:
    playingTime = i
    total += i
expectedPlayingTime = total/10
print("Expected playing time per game (number of bets made) " + str(playingTime))
total = 0
for i in expectedPlayingTimeArr:
    total += (i - expectedPlayingTime) ** 2
playingTimeVariance = total/9

total = 0
for i in expectedPropOfGamesWonArr:
    propOfGamesWon = i
    total += i
expectedPropOfGamesWon = total/10
print("Proportion of games won: " + str(propOfGamesWon))
total = 0
for i in expectedPropOfGamesWonArr:
    total += (i - expectedPropOfGamesWon) ** 2
propOfGamesWonVariance = total / 9

print("Max amount lost: $" + str(abs(maxLost)))
print("Max amount won: $" + str(maxWon))
print("Expected winnings variance: " + str(winningsVariance))
print("Expected playing time variance per game: " + str(playingTimeVariance))
print("Proportion of games won variance : " + str(propOfGamesWonVariance))


runningWinningsAverage = []
runningWinningsVariance = []
repetitions = []
for i in range(2, reps):
    repetitions.append(i)
    totalAverage = 0.0
    totalVariance = 0.0
    length = 0
    for j in range(i):
        totalAverage += winningsArr[j]
        length += 1
    totalAverage /= length
    runningWinningsAverage.append(totalAverage)
    length = 0
    for j in range(i):
        totalVariance += (winningsArr[j] - totalAverage) ** 2
        length += 1
    totalVariance /= (length - 1)
    runningWinningsVariance.append(totalVariance)

plt.plot(repetitions, runningWinningsAverage, label="Running average of winnings")
plt.plot(repetitions, runningWinningsVariance, label="Running variance of winnings")
plt.xlabel("Repetitions of game")
plt.ylabel("Values")
plt.title("Running average and variance of winnings!")
plt.legend()
plt.show()

runningWinsAvg = []
runningWinsVar = []
for i in range(2, reps):
    totalAverage = 0
    totalVariance = 0
    length = 0
    for j in range(i):
        totalAverage += gamesWonArr[j]
        length += 1
    totalAverage /= length
    runningWinsAvg.append(totalAverage)
    length = 0
    for j in range(i):
        totalVariance += (gamesWonArr[j] - totalAverage) ** 2
        length += 1
    totalVariance /= length - 1
    runningWinsVar.append(totalVariance)

plt.plot(repetitions, runningWinsAvg, label="Running average of wins")
plt.plot(repetitions, runningWinsVar, label="Running variance of wins")
plt.xlabel("Repetitions of game")
plt.ylabel("Values")
plt.title("Running average and variance of wins!")
plt.legend()
plt.show()
