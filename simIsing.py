__author__ = 'Siri'

import math, random, copy


tempS = 40 # temperatur ved start
temp = tempS # temperatur
n = 50 # lengde
neighbor = [[0 for i in range(n)]for j in range(2)]
start = [0 for i in range(n)]
kT = tempS*(1.38064852e23)
maxProb = math.exp(-4/kT)

for i in range(n):
    randomFloat = random.uniform(0,1)
    if randomFloat < 0.5:
        start[i]=-1
    else:
        start[i]=1

current = copy.copy(start)

#print neighbor
#print line_change(start)
# start = random.randint(-1, 1) for r in range(n)
# start = random.choice([1, -1] ,[n,1]) # tilfeldig modell


for i in range(0, n):
    neighbor[0][i] = i-1
    neighbor[1][i] = i+1
    if i == 0:
        neighbor[0][i]=n-1
    if i == n-1:
        neighbor[1][i]=0

prob = math.exp(-4/temp)

while temp != 0:


    for i in range(0,n):
        if current[i] != current[neighbor[0][i]] or current[i] != current[neighbor[1][i]]:
            randomNumber = random.uniform(0, maxProb)
            if randomNumber < prob:
                current[i] = -1*current[i]

    temp = temp-0.5
    #print temp

def line_change(myList):
    for i in range(n):
        if myList[i] == 1:
            myList[i] = "+"
        if myList[i] == -1:
            myList[i] = "-"
    return myList


print "  "
new_start = (line_change(start))

pretty = ""
for i in new_start:
    pretty += "{:3s}".format(i)
print pretty

print '  '
new_current = (line_change(current))

ugly = ""
for i in new_current:
    ugly += "{:3s}".format(i)
print ugly
