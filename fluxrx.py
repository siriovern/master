__author__ = 'Siri'

import math, random
import matplotlib.pyplot as plt
import numpy as np

# boltzmann at start
kT = 10
#number of cycles
n = 1000
#number of trials per cycle
m = 50
#boltzmann at the end
kTend = 0.5
#fractional reduction every cycle
fract = (kTend/kT)**(1.0/(n-1.0))

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
            #godta uansett
            value = reactions
        if reactionsNew >= 2000:
            #godta uansett
            value = reactions

    return (reactionsNew, value)

#best results so far
allReactions = []
allTemperatures = []
stDev = []

for i in range(n):

    for j in range(m):

        new, rxValue = numreactions(current)
        deltaE = abs(start-rxValue)
        prob = math.exp(-deltaE/kT)
        if (random.random()<prob):
            avgList.append(new)
        else:
            continue


    if np.mean(avgList) == 0:
        allReactions.append(avgNumber)
    else:
        avgNumber = np.mean(avgList)
        allReactions.append(avgNumber)
    avgList = []
    current = avgNumber
    xAxis = (1.0/kT)
    allTemperatures.append(xAxis)
    #if kT >= kTend:
    kT = kT * fract

    stdevValue = np.std(allReactions)
    stDev.append(stdevValue)


print allReactions
print allTemperatures
print stDev

rx = plt.figure()
plt.scatter(allTemperatures,allReactions, s=1)
plt.axis([0,2,1994,2002])
plt.xlabel('1/T')
plt.ylabel('number of reactions')
plt.axhline(y=2000,c="blue",linewidth=0.5,zorder=0)

st = plt.figure()
plt.plot(allTemperatures,stDev)
plt.xlabel('1/T')

plt.show()
