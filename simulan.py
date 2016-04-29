__author__ = 'Siri'

import math, random
import matplotlib.pyplot as plt
import numpy as np

# boltzmann at start
kT = 10
#number of cycles
n = 90
#number of trials per cycle
m = 50
#boltzmann at the end
kTend = 1

avgList = list()
start = 2000
current = start


def numreactions(reactions):

    randomNumber = random.random()
    value = reactions
    # legger til en reaksjon
    if randomNumber >= 0.5:
        reactionsNew = reactions + 1
        if reactionsNew < 2000:
            #godta uansett
            value = reactions
        if reactionsNew >= 2000:
            #som vanlig
            value = reactionsNew
    else:
        reactionsNew = reactions - 1
        if reactionsNew < 2000:
            #som vanlig
            value = reactionsNew
        if reactionsNew >= 2000:
            #godta uansett
            value = reactions

    return (reactionsNew, value)

#best results so far
allReactions = [0] * n
allTemperatures = [0] * n


for i in range(n):
    while kT >= kTend:
        for j in range(m):

            new, rxValue = numreactions(current)
            deltaE = abs(start-rxValue)
            prob = math.exp(-deltaE/kT)
            if (random.random()<prob):
                current = new
                avgList.append(current)
            else:
                continue

        avgNumber = np.mean(avgList)
        avgList = []
        allReactions[i] = avgNumber
        xAxis = (1/kT)
        allTemperatures[i] = xAxis
        kT = kT-0.1

stdev = [0]*n
#stdev
#for i in range(n):
 #   stdev[i] =

print allReactions
print allTemperatures

plt.scatter(allTemperatures,allReactions)
plt.axis([0,1, 1990,2010])
plt.show()

