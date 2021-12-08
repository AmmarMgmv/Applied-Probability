import random as r
import pandas as p
import numpy as np
import plotly as pl
import matplotlib.pyplot as plt

OrganisedCards = []
for i in range(1, 101):
    OrganisedCards.append(i)

def playGame(cards):
    r.shuffle(cards)
    matches = 0
    for y in range(100):
        if y == cards[y]:
            matches += 1
    return matches

Results = []
for x in range(10000):
    value = playGame(OrganisedCards)
    Results.append(value)

print("Expected number of hits: " + str(np.mean(Results)))
print("Variance of hits over 10000 simulations: " + str(np.var(Results, ddof=1)))


