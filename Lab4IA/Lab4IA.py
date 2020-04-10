from AlgGen import *

pop=initPop()
cr=alg(pop)
print("Cel mai scurt drum este:")
for x in cr.getRepres():
    print(x)
print("Distanta este: "+str(cr.getDistanta()))

