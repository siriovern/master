__author__ = 'Siri'

import random
import cobra
import copy
#import gurobipy
import cobra.io.mat

#from cobra import Reaction
#from cobra import solvers
global startBlocked
global endBlocked
global blockedTimes
#from cobra.io.mat import model_to_pymatbridge
import time

#salmonella = cobra.test.create_test_model(cobra.test.salmonella_pickle)
tuberculosis = cobra.io.read_sbml_model('C:\Users\Siri\SkyDrive\NTNU\_master\igg_iNJ661.COBRA-sbml3.xml')

model = copy.copy(tuberculosis)

universe = cobra.io.read_sbml_model('C:\Users\Siri\SkyDrive\NTNU\_master\universe_mnx.xml')

lastModel = model
react = model.reactions[0]



def biomassproduced(currentmodel):
    currentmodel.optimize()
    if currentmodel.solution.status == 'optimal':
        return True #produces biomass
    else:
        return False


def lastmodel():
    model = copy.deepcopy(lastModel)
    return len(lastModel.reactions)


def updatelast(mod):
    #FINN: inserted timers
    #startBlocked = time.time()
    lastMod = copy.deepcopy(mod)
    #endBlocked = time.time()
    #FINN: for profiling
    #print(str(endBlocked - startBlocked) + ",")
    return lastMod


def addreaction():
    nUniverse = len(universe.reactions)
    global lastModel
    lastModel = updatelast(model)
    #FINN: removed this because yolo
    #lastUniverse = updatelast(universe)
    reactionNr = random.randint(0, nUniverse-1) #velger tilfeldig reaksjon
    react = (universe.reactions[reactionNr]) #velger tilfeldig reaksjon i universet
    model.add_reaction(react) #legger til reaksjon i modell
    return len(model.reactions)


def removereaction():
    global lastModel
    lastModel = updatelast(model)
    #lastUniverse = updatelast(universe)
    biomassProduced = 0

    while biomassProduced == 0:
        reactionNr = random.randint(0, len(model.reactions)-1)
        react = (model.reactions[reactionNr]) #velger tilfeldig reaksjon i universet
        universe.add_reaction(react) #legger til reaksjon i modell
        model.reactions.remove(react) #fjerner reaksjon fra univers
        stillproducingbiomass = biomassproduced(model)
        if stillproducingbiomass == True:
            biomassProduced = 1
        else:
            universe.reactions.remove(react)
            model.add_reaction(react)
    return len(model.reactions)


def numberofblockedreactions():
    model.optimize()
    blockedReactions = 0
    for i in range(0,len(model.reactions)-1):
        reaction = copy.deepcopy(model.reactions[i])
        upper = reaction.upper_bound
        lower = reaction.lower_bound
        if upper == 0 and lower == 0:
            blockedReactions += 1
    return blockedReactions #returns number of blocked reactions

