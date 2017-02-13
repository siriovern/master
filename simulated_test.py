__author__ = 'Siri'

from numbercheck import numberchecker
import math
import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import pyplot

temp = 500
ideal = 1000
modelNumber = ideal
n = 1000
r= 0

allReactions = []
allTemperatures = []
stDev = []
temperatures = []
rejects = []

while temp > 2:
    temper = (1.0/temp)
    temperatures.append(temper)

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
                        r += 1
            else:
                if delta == 1:
                    if randomNumber > p1:
                        modelNumber = modelLast
                        r+=1


        xAxis = (1.0/temp)
        allReactions.append(modelNumber)
        allTemperatures.append(xAxis)




    #allTemperatures.append(xAxis)
    temp = temp-0.5
    rejects.append(r)
    r=0
    #print temp

print temperatures
print rejects

rx = plt.figure()
plt.scatter(allTemperatures,allReactions, s=1)

plt.axis([0.001,1,910,1080])
plt.xlabel('1/T')
plt.ylabel('number of reactions')
plt.axhline(y=ideal,c="blue",linewidth=0.5,zorder=0)
pyplot.xscale('log')

ax2 = plt.twinx()
ax2.plot(temperatures, rejects, 'r-')
ax2.set_ylabel('rejects', color='r')
ax2.tick_params('y', colors='r')

plt.show()