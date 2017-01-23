__author__ = 'Siri'

from numbers import numberchecker
import math
import random

temp = 100
ideal = 1000
modelNumber = ideal
n = 500


while temp > 0:

    for i in range(1,n):

        modelLast = modelNumber
        [modelNumber, delta] = numberchecker(modelNumber)

        if modelNumber != ideal:

            deltaN = math.fabs(ideal-modelNumber)
            p1 = math.exp(-deltaN/temp) # sannsynlighet som funksjon av t1
            randomNumber = random.random()

            if modelNumber < ideal:
                if delta == 1:
                    continue
                else:
                    if randomNumber > p1:
                        modelNumber = modelLast
                    else:
                        continue
            else:
                if delta == 1:
                    if randomNumber > p1:
                        modelNumber = modelLast
                    else:
                        continue
                else:
                    continue

        if modelNumber == ideal:
            continue

    temp = temp-1

print modelNumber