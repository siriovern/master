__author__ = 'Siri'

import random
import cobra.test
#from cobra.io.mat import model_to_pymatbridge

import pandas
#model_to_pymatbridge(m, variable_name="model")

model = cobra.test.create_test_model(cobra.test.salmonella_pickle)
# laste inn naavaerende modell
# laste inn univers

def numberofreactions():


    numberReactions = len(model.reactions) # antall reaksjoner i model

    biomass = model.objective # = 1 hvis modellen produserer biomass
    opt = model.optimize()

    print 'her kommer opt.f:'
    print opt.f
    print model.solution.f

    print biomass

   # if biomass == 'Reaction biomass_iRR1083_metals at 0x75f9790>: 1.0':
    #    print 'hurra'

    addOrRemove = random.random()

    if addOrRemove >= 0.5:
        # add reaction
        print numberReactions
    else:
        # remove reaction
        # kan modellen fremdeles produsere biomass?
        print numberReactions


    return (numberReactions)

def numberofblockedreactions():

    # finn antall blokkerte raksjoner fra navaerende modell M
    # enklest: sjekke flux for ALLE reaksjoner (veldig tregt!)
    blockedReactions = 1

    return(blockedReactions)


n =  numberofreactions()
print n