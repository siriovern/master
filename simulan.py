__author__ = 'Siri'

import math, random
import matplotlib.pyplot as plt
import numpy as np

# boltzmann at start
kT = 10
#number of cycles
n = 4000
#number of trials per cycle
m = 20
#boltzmann at the end
kTend = 1.0
#fractional reduction every cycle
fract = (kTend/kT)**(1.0/(n-1.0))

avgList = list()
start = 2000
current = start


def numreactions(reactions):

    randomNumber = random.random()
    #value = reactions
    # legger til en reaksjon
    if randomNumber >= 0.5:
        reactionsNew = reactions + 1
        if reactionsNew < 2000:
            #godta uansett
            value = -1
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
            value = -1

    return (reactionsNew, value)

#best results so far
allReactions = []
allTemperatures = []
stDev = []

for i in range(n):
    for j in range(m):
        new, rxValue = numreactions(current)
        if rxValue == -1:
            avgList.append(new)
        else:
            deltaE = abs(current-new)
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
    if kT >= kTend:
        kT = kT * fract

    stdevValue = np.std(allReactions)
    stDev.append(stdevValue)

print allReactions
print allTemperatures
print stDev

rx = plt.figure()
plt.scatter(allTemperatures,allReactions, s=1)
plt.axis([0,1.1,1998,2003])
plt.xlabel('1/T')
plt.ylabel('number of reactions')
plt.axhline(y=2000,c="blue",linewidth=0.5,zorder=0)

st = plt.figure()
plt.plot(allTemperatures,stDev)
#plt.axis([0,1.1, 0,0.5])
plt.xlabel('1/T')

plt.show()


