__author__ = 'Siri'

import math, random

# boltzmann at start
kT = 10
#number of cycles
n = 50
#boltzmann at the end
kTend = 1

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

for i in range(n):
    new, reactionvalue = numreactions(current)
    deltaE = abs(start-reactionvalue)
    prob = math.exp(-deltaE/kT)
    if (random.random()<prob):
        current = new
    allReactions[i] = current
    kT = kT-0.1

print allReactions

