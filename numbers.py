__author__ = 'Siri'

import random


# skal virke som cobra_code, men bare spytte ut tall i stedet for a styre med faktisk modell


def numberchecker(myNumber):
    addOrRemove = random.random()

    if addOrRemove < 0.5:
        myNumber = myNumber+1
        delta = 1
    else:
        myNumber = myNumber -1
        delta = -1

    return myNumber, delta


