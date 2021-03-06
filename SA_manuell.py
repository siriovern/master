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

temp1 = [500, 300, 100, 75, 50, 40, 15, 10, 7, 5, 1] # eksempeltemperaturer
temp2 = 50 # for blokkerte reaksjoner. Holdes konstant
optimalReactions = 1029 # onsket antall reaksjoner
optimalBlocked = 3 # maks antall blokkerte reaksjoner
n=3 #Antall sykler per temp. Like mange som antall reaksjoner i opprinnelig modell?
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

blockedTimes = []

for j in range(0, len(temp1)):
    #FINN: removed printstatements
    temp = temp1[j]
    addtolist = (1.0/temp) #x-akse plot
    temperatures.append(addtolist)

    for i in range(n):
        xakse.append(addtolist)
        if  random.random() > 0.5: # 50% sannsynlighet
            #legg til reaksjon
            antallRxScenario += 1
            deltaN = math.fabs(optimalReactions-antallRxScenario)
            probability = math.exp(-deltaN/temp) # sannsynlighet som funksjon av temp
            if nReactions < optimalReactions: #godta uansett
                nReactions = addreaction()
                addedreactions += 1 #total number of added reactions
            else:
                if  random.random() < probability:
                    nReactions = addreaction() #add reaction
                    addedreactions += 1 #total number of added reactions
                else:
                    antallRxScenario -= 1
                    rejects += 1 #total number of rejects

        else:
            # trekke fra reaksjon
            antallRxScenario -= 1
            deltaN = math.fabs(optimalReactions-antallRxScenario)
            probability = math.exp(-deltaN/temp) # sannsynlighet som funksjon av t1
            if nReactions > optimalReactions: #fjern uansett
                nReactions = removereaction()
                removedreactions += 1 #number of removed reactions
            else:
                if  random.random() < probability:
                    nReactions = removereaction()
                    removedreactions += 1
                else:
                    antallRxScenario -= 1
                    rejects += 1

        reactions.append(nReactions)

        nBlocked = numberofblockedreactions() #number of blocked reactions in model
        if nBlocked > optimalBlocked: #too many blocked reactions
            deltaB = optimalBlocked-nBlocked
            probability2 = math.exp(deltaB/temp2)
            if random.random() > probability2: 
                #FINN: example of time profiling
                #startBlocked = time.time()
                nBlocked = lastmodel()
                #endBlocked = time.time()
                #blockedTimes.append(endBlocked - startBlocked)
                rejects += 1
                # forkast sletting av reaksjon
    allrejects.append(rejects)
    rejects = 0

print nReactions
print nBlocked
endTime = time.time()
print 'sekunder: %s' % (time.time()-startTime)


# KUN FOR PLOT:
#print xakse
#print reactions
#print allrejects

rx = plt.figure()
plt.scatter(xakse,reactions, s=1)

plt.axis([0.001,1,1000,1050])
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
#FINN: did some timing
#print("times: ", blockedTimes)
#finnsum = 0
#for elem in blockedTimes:
#    finnsum += elem
#avg = finnsum/len(blockedTimes)
#print("average block time: ", avg)
#print("time spent in bottleneck: ", finnsum)
#print("block as a percentage of runtime: ", (finnsum/endTime)*100)