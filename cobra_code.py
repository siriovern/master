__author__ = 'Siri'

import random
import cobra.test
import pandas

model = cobra.test.create_test_model(cobra.test.salmonella_pickle)

def numberofreactions():

    numberReactions = len(model.reactions) # antall reaksjoner i model

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