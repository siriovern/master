__author__ = 'Siri'


import math
import random
import time

from cobra_code import numberofreactions
from cobra_code import numberofblockedreactions

from cobra_code import lastmodel

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import pyplot

startTime=time.time()

temp1 = [500, 300, 100, 50, 30, 15, 10, 7, 5, 3, 1, 0.1] # for antall reaksjoiner
temp2 = 1 # for blokkerte reaksjoner. Holdes konstant
optimalReactions = 1029 # onsket antall reaksjoner
optimalBlocked = 14 # maks antall blokkerte reaksjoner
n=10 #Antall sykler per temp. Like mange som antall reaksjoner i opprinnelig modell?
nReactions = 1029
nBlocked =0

xakse = []
reactions = []
rejects = []


for j in range(0, len(temp1)):
    print j
    temp = temp1[j]
    print temp
    addtolist = (1.0/temp)

    for i in range(n):
        deltaN = math.fabs(optimalReactions-nReactions)
        p1 = math.exp(-deltaN/temp) # sannsynlighet som funksjon av t1
        randomNumber1 = random.random()

        addorRemove = random.random()

        if addorRemove > 0.5:
            #legg til reaksjon

        xakse.append(addtolist)
        nReactions, delta = numberofreactions() #kaller funksjon fra cobra_code
        nBlocked = numberofblockedreactions()
        if nReactions != optimalReactions:
            deltaN = math.fabs(optimalReactions-nReactions)
            p1 = math.exp(-deltaN/temp) # sannsynlighet som funksjon av t1
            randomNumber1 = random.random()

            if nReactions < optimalReactions:
                if delta != 1: #velg forrige modell, kanskje
                    if randomNumber1 > p1:
                        nReactions = lastmodel()

            elif nReactions > optimalReactions:
                if delta == 1: #velg forrige modell,kanskje
                    if randomNumber1 > p1:
                     nReactions = lastmodel()

        reactions.append(nReactions)

        if nBlocked > optimalBlocked:
            deltaB = optimalBlocked-nBlocked
            p2 = math.exp(deltaB/temp2)
            randomNumber2 = random.random()
            if randomNumber2 > p2:
                nBlocked = lastmodel()
                # forkast sletting av reaksjon

print xakse
print reactions
rx = plt.figure()
plt.scatter(xakse,reactions, s=1)

#plt.axis([0.001,1,910,1080])
plt.xlabel('1/T')
plt.ylabel('number of reactions')
plt.axhline(y=optimalReactions,c="blue",linewidth=0.5,zorder=0)
pyplot.xscale('log')
plt.show()
print nReactions
print nBlocked
print 'sekunder: %s' % (time.time()-startTime)