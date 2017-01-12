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
lastModel = model.copy()
react = model.reactions[0]
lastUniverse = universe.copy()


def biomassproduced(currentmodel):
    currentmodel.optimize()
    if currentmodel.solution.status == 'optimal':
        return True
    else:
        return False


def lastmodel():
    universe = lastUniverse.copy()
    model = lastModel.copy()
    return (len(lastModel.reactions))


def updatelast(mod):
    lastMod = mod.copy()
    return lastMod


def numberofreactions():
    addOrRemove = random.random()
    nModel = len(model.reactions)
    nUniverse = len(universe.reactions)
    lastModel = updatelast(model)
    lastUniverse = updatelast(universe)
    if addOrRemove >= 0.5: # add reaction
        reactionNr = random.randint(0, nUniverse-1)
        react = (universe.reactions[reactionNr]) #velger tilfeldig reaksjon i universet
        model.add_reaction(react) #legger til reaksjon i modell
        universe.reactions.remove(react) #fjerner reaksjon fra univers
        mModel = len(model.reactions) #sjeker ny lengde
        #mUniverse =  len(universe.reactions)
    else:
        biomassProduced = 0

        while biomassProduced == 0:
            reactionNr = random.randint(0, len(model.reactions)-1)
            react = (model.reactions[reactionNr]) #velger tilfeldig reaksjon i universet
            #print 'fjerner reaksjon nr %i i modell med %i reaksjoner' %(reactionNr, len(model.reactions))
            universe.add_reaction(react) #legger til reaksjon i modell
            model.reactions.remove(react) #fjerner reaksjon fra univers
            #print 'la til reaksjon. naa er det: %i' %(len(model.reactions))
            mModel = len(model.reactions) #sjeker ny lengde
            #mUniverse =  len(universe.reactions) #ny lengde univers
            stillproducingbiomass = biomassproduced(model)
            if stillproducingbiomass == True:
                biomassProduced = 1
            else:
                print len(model.reactions)
                universe.reactions.remove(react)
                model.add_reaction(react)
                print 'La reaksjon tilbake igjen. Modellen har fremdeles %i reaksjoner. HURRA' %(len(model.reactions))

    return mModel


def numberofblockedreactions():
    blockedReactions = 0
    nModel = len(model.reactions)
    for i in range(0,nModel-1):
        reaction = copy.deepcopy(model.reactions[i])
        upper = reaction.upper_bound
        lower = reaction.lower_bound
        if upper == 0 and lower == 0:
            blockedReactions += 1
    return(blockedReactions)


#n =  numberofreactions()
#print n

#m = numberofblockedreactions()
#print m