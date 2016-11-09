__author__ = 'Siri'


import math
import random
from cobra_code import numberofreactions
from cobra_code import numberofblockedreactions

temp1 = 1 # for antall reaksjoiner
temp2 = 1 # for blokkerte reaksjoner. Holdes konstant

optimalReactions = 1 # onsket antall reaksjoner
optimalBlocked = 1 # maks antall blokkerte reaksjoner


n=1 # Antall sykler per temp. Like mange som antall reaksjoner i opprinnelig modell?

while temp1 != 0:

    for i in range(n):
        nReactions = numberofreactions() #kaller funksjon fra cobra_code
        nBlocked = numberofblockedreactions()
        if nReactions != optimalReactions:
            deltaN = math.fabs(optimalReactions-nReactions)
            p1 = math.exp(-deltaN/temp1) # sannsynlighet som funksjon av t1
            randomNumber1 = random.random()
            if randomNumber1 > p1:
                print nReactions
                # forkast sletting av reaksjon
            else:
                # behold endringer
                print nReactions
        else:
            print nReactions
            # keep

        if nBlocked > optimalBlocked:
            deltaB = optimalBlocked-nBlocked
            p2 = math.exp(deltaB/temp2)
            randomNumber2 = random.random()
            if randomNumber2 > p2:
                print nBlocked
                # forkast sletting av reaksjon
            else:
                print nBlocked
                # behold endringer
        else:
            print nBlocked
            # keep
    temp1 = temp1 -0.1

