
from Chromosome import *
popSize=1000
noIter=100  

def initPop():
    pop=[]
    for _ in range(0,popSize):
        cr=Chromosome()
        pop.append(cr)
    return pop
   

def selection(pop):

    index=randint(0,len(pop)-1)
    return pop[index]

def best(list):
    cr = list[0];
    fitness =    cr.getFitness();
    for c in list:
        if (c.getFitness() < fitness): 
            fitness =c.getFitness();
            cr = c;
    return cr;

def alg(pop):
    list = []
    pop = initPop()
    for i in range(0,noIter):
        newPop = []
        for  i in range(0,len(pop)):
           cr1 = selection(pop);
           cr2 = selection(pop);
           cr3 = cr1.crossover(cr2);
           mut = cr3.mutation();
         
           newPop.append(mut);
        list.append(best(newPop));
        pop = newPop;
    return best(list);   
