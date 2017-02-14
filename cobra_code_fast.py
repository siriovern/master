__author__ = 'Siri'

import random
import cobra.test
import copy
import gurobipy
#from cobra import Reaction
#from cobra import solvers

#from cobra.io.mat import model_to_pymatbridge

#import pandas
#model_to_pymatbridge(m, variable_name="model")

#salmonella = cobra.test.create_test_model(cobra.test.salmonella_pickle)
tuberculosis = cobra.io.read_sbml_model('C:\Users\Siri\SkyDrive\NTNU\_master\igg_iNJ661.COBRA-sbml3.xml')

model = copy.copy(tuberculosis)

universe = cobra.io.read_sbml_model('C:\Users\Siri\SkyDrive\NTNU\_master\universe_mnx.xml')

lastModel = model
react = model.reactions[0]
lastUniverse = universe


def biomassproduced(currentmodel):
    currentmodel.optimize(gurobipy)
    if currentmodel.solution.status == 'optimal':
        return True
    else:
        return False


def lastmodel():
    universe = copy.deepcopy(lastUniverse)
    model = copy.deepcopy(lastModel)
    return (len(lastModel.reactions))


def updatelast(mod):
    lastMod = copy.deepcopy(mod)
    return lastMod


def addreaction():
    nModel = len(model.reactions)
    nUniverse = len(universe.reactions)
    print nModel
    global lastModel
    global lastUniverse
    lastModel = updatelast(model)
    lastUniverse = updatelast(universe)

    reactionNr = random.randint(0, nUniverse-1)
    react = (universe.reactions[reactionNr]) #velger tilfeldig reaksjon i universet
    model.add_reaction(react) #legger til reaksjon i modell
    universe.reactions.remove(react) #fjerner reaksjon fra univers
    mModel = len(model.reactions) #sjeker ny lengde

    return mModel


def removereaction():
    nModel = len(model.reactions)
    nUniverse = len(universe.reactions)
    print nModel
    global lastModel
    global lastUniverse
    lastModel = updatelast(model)
    lastUniverse = updatelast(universe)
    biomassProduced = 0

    while biomassProduced == 0:
        reactionNr = random.randint(0, len(model.reactions)-1)
        react = (model.reactions[reactionNr]) #velger tilfeldig reaksjon i universet
        universe.add_reaction(react) #legger til reaksjon i modell
        model.reactions.remove(react) #fjerner reaksjon fra univers
        mModel = len(model.reactions) #sjeker ny lengde
        stillproducingbiomass = biomassproduced(model)
        if stillproducingbiomass == True:
            biomassProduced = 1
        else:
            print len(model.reactions)
            universe.reactions.remove(react)
            model.add_reaction(react)
    return mModel

def numberofreactions():

    addOrRemove = random.random()
    nModel = len(model.reactions)
    nUniverse = len(universe.reactions)
    print nModel
    global lastModel
    global lastUniverse
    lastModel = updatelast(model)
    lastUniverse = updatelast(universe)
    if addOrRemove >= 0.5: # add reaction
        reactionNr = random.randint(0, nUniverse-1)
        react = (universe.reactions[reactionNr]) #velger tilfeldig reaksjon i universet
        model.add_reaction(react) #legger til reaksjon i modell
        universe.reactions.remove(react) #fjerner reaksjon fra univers
        mModel = len(model.reactions) #sjeker ny lengde
        #mUniverse =  len(universe.reactions)
        delta = 1
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
            delta = 0
            if stillproducingbiomass == True:
                biomassProduced = 1
            else:
                print len(model.reactions)
                universe.reactions.remove(react)
                model.add_reaction(react)

    return mModel, delta


def numberofblockedreactions():
    model.optimize(gurobipy)
    blockedReactions = 0
    nModel = len(model.reactions)
    for i in range(0,nModel-1):
        reaction = copy.deepcopy(model.reactions[i])
        upper = reaction.upper_bound
        lower = reaction.lower_bound
        if upper == 0 and lower == 0:
            blockedReactions += 1
    return(blockedReactions)
