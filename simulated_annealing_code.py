__author__ = 'Siri'

import math
import random
from cobra_code import numberOfReactions
from cobra_code import numberOfBlockedReactions

temp1 = 1 # for antall reaksjoiner
temp2 = 1 # for blokkerte reaksjoner. Holdes konstant

optimalReactions = 1 # onsket antall reaksjoner
optimalBlocked = 1 # maks antall blokkerte reaksjoner


n=50 # Antall sykler per temp. Like mange som antall reaksjoner i opprinnelig modell?

while temp1 != 0:

    for i in range(n):
        nReactions = numberOfReactions() #kaller funksjon fra cobra_code
        nBlocked = numberOfBlockedReactions()
        if nReactions != optimalReactions:
            deltaN = math.fabs(optimalReactions-nReactions)
            p1 = math.exp(-deltaN/temp1) # sannsynlighet som funksjon av t1
            randomNumber1 = random.random
            if randomNumber1 > p1:
                # forkast sletting av reaksjon
            else:
                # behold endringer
        else:
            # keep

        if nBlocked > optimalBlocked:
            deltaB = optimalBlocked-nBlocked
            p2 = math.exp(deltaB/temp2)
            randomNumber2 = random.random
            if randomNumber2 > p2:
                # forkast sletting av reaksjon
            else:
                # behold endringer
        else:
            # keep
    temp1 = temp1 -0.1

