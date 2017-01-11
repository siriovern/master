__author__ = 'Siri'


import math
import random
from cobra_code import numberofreactions
from cobra_code import numberofblockedreactions

from cobra_code import lastmodel

temp1 = 100000 # for antall reaksjoiner
temp2 = 1 # for blokkerte reaksjoner. Holdes konstant
optimalReactions = 2546 # onsket antall reaksjoner
optimalBlocked = 14 # maks antall blokkerte reaksjoner
n=1 # Antall sykler per temp. Like mange som antall reaksjoner i opprinnelig modell?


while temp1 != 0:

    for i in range(n):
        #lastSolution = nReactions
        nReactions = numberofreactions() #kaller funksjon fra cobra_code
        nBlocked = numberofblockedreactions()
        if nReactions != optimalReactions:
            deltaN = math.fabs(optimalReactions-nReactions)
            p1 = math.exp(-deltaN/temp1) # sannsynlighet som funksjon av t1
            randomNumber1 = random.random()
            if randomNumber1 > p1:
                lastSolution = lastmodel()
                print 'ingen endring. Fremdeles: %i' % (lastSolution)
                # ikke aksepter endring
            else:
                print 'printer ny modell: %i' %(nReactions) #keep
        else:
            print 'Optimalt antall reaksjoner: %i' %(nReactions)
            # keep

        if nBlocked > optimalBlocked:
            deltaB = optimalBlocked-nBlocked
            p2 = math.exp(deltaB/temp2)
            randomNumber2 = random.random()
            if randomNumber2 > p2:
                nBlocked = lastmodel()
                print nBlocked
                # forkast sletting av reaksjon
            else:
                print nBlocked
                # behold endringer
        else:
            print nBlocked
            # keep
    temp1 = temp1 - 1000

