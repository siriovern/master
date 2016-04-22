__author__ = 'Siri'

from math import exp
from random import random

def anneal(solution):

    T = getTemperature()

    current_cost = createInitialSolution(Problemsize)
    best_cost = current_cost
    new_cost = createNeighborSolution(current_cost)

    if new_cost < current_cost:
        current_cost = new_cost
        if new_cost < best_cost:
            best_cost = current_cost


    dE = current_cost - new_cost
    e = exp(dE/T)

    if e > random():
        current_cost = new_cost

    return best_cost

