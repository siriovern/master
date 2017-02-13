__author__ = 'Siri'


import math
import random
import time

from cobra_code_fast import addreaction
from cobra_code_fast import removereaction
from cobra_code_fast import numberofblockedreactions
from cobra_code_fast import lastmodel

#import numpy as np
import matplotlib.pyplot as plt
from matplotlib import pyplot

startTime=time.time()

temp1 = [500, 300, 100, 75, 50, 40, 30, 15, 10, 7, 5, 1] # for antall reaksjoiner
temp2 = 1 # for blokkerte reaksjoner. Holdes konstant
optimalReactions = 1029 # onsket antall reaksjoner
optimalBlocked = 14 # maks antall blokkerte reaksjoner
n=50 #Antall sykler per temp. Like mange som antall reaksjoner i opprinnelig modell?
nReactions = 1029
nBlocked =0

antallRxScenario = optimalReactions
addedreactions = 0
removedreactions = 0
rejects = 0

xakse = []
reactions = []
allrejects = []
temperatures = []


for j in range(0, len(temp1)):
    print j
    temp = temp1[j]
    print temp
    addtolist = (1.0/temp)
    temperatures.append(addtolist)

    for i in range(n):
        xakse.append(addtolist)
        randomNumber1 = random.random()
        addorRemove = random.random()
        if addorRemove > 0.5:
            #legg til reaksjon
            antallRxScenario += 1
            deltaN = math.fabs(optimalReactions-antallRxScenario)
            p1 = math.exp(-deltaN/temp) # sannsynlighet som funksjon av t1
            if nReactions < optimalReactions:
                nReactions = addreaction()
                addedreactions += 1
            else:
                if randomNumber1 < p1:
                    nReactions = addreaction()
                    addedreactions += 1
                else:
                    antallRxScenario -= 1
                    rejects += 1

        else:
            # trekke fra reaksjon
            antallRxScenario -= 1
            deltaN = math.fabs(optimalReactions-antallRxScenario)
            p1 = math.exp(-deltaN/temp) # sannsynlighet som funksjon av t1

            if nReactions > optimalReactions:
                nReactions = removereaction()
                removedreactions += 1
            else:
                if randomNumber1 < p1:
                    nReactions = removereaction()
                    removedreactions += 1
                else:
                    antallRxScenario -= 1
                    rejects += 1

        reactions.append(nReactions)
        nBlocked = numberofblockedreactions()
        if nBlocked > optimalBlocked:
            deltaB = optimalBlocked-nBlocked
            p2 = math.exp(deltaB/temp2)
            randomNumber2 = random.random()
            if randomNumber2 > p2:
                nBlocked = lastmodel()
                rejects += 1
                # forkast sletting av reaksjon
    allrejects.append(rejects)
    rejects = 0

print xakse
print reactions
print allrejects

rx = plt.figure()
plt.scatter(xakse,reactions, s=1)

plt.axis([0.001,1,940,1070])
plt.xlabel('1/T')
plt.ylabel('number of reactions')
plt.axhline(y=optimalReactions,c="blue")
#plt.plot(temperatures,allrejects)
pyplot.xscale('log')
ax2 = plt.twinx()
ax2.plot(temperatures, allrejects, 'r-')
ax2.set_ylabel('rejects', color='r')
ax2.tick_params('y', colors='r')
plt.show()
print nReactions
print nBlocked
print 'sekunder: %s' % (time.time()-startTime)