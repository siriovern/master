__author__ = 'Siri'

import random
import cobra.test
import copy
from cobra import Reaction
#from cobra import solvers

#from cobra.io.mat import model_to_pymatbridge

#import pandas
#model_to_pymatbridge(m, variable_name="model")

salmonella = cobra.test.create_test_model(cobra.test.salmonella_pickle)
model = copy.copy(salmonella)
universe = cobra.io.read_sbml_model('C:\Users\Siri\SkyDrive\NTNU\_master\universe_mnx.xml')

def biomassproduced(currentModel):
    currentModel.optimize()
    print 'er inne i drittfunksjonen'
    print currentModel.solution.f
    if currentModel.solution.status == 'optimal':
        return True
    else:
        return False

def numberofreactions():

    biomass = model.objective # = 1 hvis modellen produserer biomass
    print 'biomass: 1 if biomass:'
    print biomass

    addOrRemove = random.random()
    nModel = len(model.reactions) # antall reaksjoner i model
    nUniverse = len(universe.reactions)

    if addOrRemove >= 0.9: # add reaction

        print 'legger til reaksjon'
        reactionNr = random.randint(1, nUniverse)
        react = (universe.reactions[reactionNr]) #velger tilfeldig reaksjon i universet
        print 'reaksjoner i modell: %d' % (nModel)
        print 'reaksjoner i univers: %d' % (nUniverse)

        model.add_reaction(react) #legger til reaksjon i modell
        universe.reactions.remove(react) #fjerner reaksjon fra univers

        mModel = len(model.reactions) #sjeker ny lengde
        print 'reaksjoner i modell er naa: %d' % (mModel)
        mUniverse =  len(universe.reactions) #ny lengde univers
        print 'reaksjoner i unvers er naa: %d' % (mUniverse)

        return mModel
    else:
        print 'fjerner reaksjon'
        biomassProduced = 0
        while biomassProduced == 0:
            reactionNr = random.randint(1, nModel)
            react = (model.reactions[reactionNr]) #velger tilfeldig reaksjon i universet
            print 'reaksjoner i modell: %d' % (nModel)
            print 'reaksjoner i univers: %d' % (nUniverse)

            universe.add_reaction(react) #legger til reaksjon i modell
            model.reactions.remove(react) #fjerner reaksjon fra univers

            mModel = len(model.reactions) #sjeker ny lengde
            print 'reaksjoner i modell er naa: %d' % (mModel)
            mUniverse =  len(universe.reactions) #ny lengde univers
            print 'reaksjoner i unvers er naa: %d' % (mUniverse)
            stillproducingbiomass = biomassproduced(model)

            if stillproducingbiomass == True:
                biomassProduced = 1

        return mModel

def numberofblockedreactions():

    # finn antall blokkerte raksjoner fra navaerende modell M
    # enklest: sjekke flux for ALLE reaksjoner (veldig tregt!)
    blockedReactions = 0
    nModel = len(model.reactions)
    for i in range(0,nModel-1):
        reaction = copy.copy(model.reactions[i])
        if reaction.lower_bound == 0 and reaction.upper_bound == 0:
            blockedReactions += 1

    return(blockedReactions)


#n =  numberofreactions()
#print n

#m = numberofblockedreactions()
#print m