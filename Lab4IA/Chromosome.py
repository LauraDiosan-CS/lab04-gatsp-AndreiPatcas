from utils import *
class Chromosome:
    def __init__(self):
        self.__problParam = net  #problParam has to store the number of nodes/cities
        self.__repres = generateARandomPermutation(self.__problParam['noNodes'])
        self.__fitness = 0.0
    
 
    def getRepres(self):
        return self.__repres 
   
  
    
   # @fitness.setter 
    def getFitness(self):
        mat=self.__problParam['matrix']
        l=self.__problParam['noNodes']
        s=0
        for i in range(0,l-1):
            nodes=self.__repres
            s=s+mat[nodes[i]][nodes[i+1]]
        return s   
    
    def getDistanta(self):
        mat=self.__problParam['matrix']
        l=self.__problParam['noNodes']
        nodes=self.__repres
        return self.getFitness()+mat[nodes[l-1]][nodes[0]]

    def crossover(self, c):
      
        repr1=self.__repres;
        repr2=c.__repres;
        newrepres=[]
        for i in range(0, len(repr1)):
            aux=repr2[i]
            newrepres.append(repr1[aux])
        
        offspring = Chromosome()
        offspring.__repres = newrepres
        return offspring
    
    def mutation(self):
       
        oldrepres=self.__repres
        pos1 = randint(0, self.__problParam['noNodes']-1)
        pos2 = randint(0, self.__problParam['noNodes']-1)
        aux=oldrepres[pos1]
        oldrepres[pos1]=oldrepres[pos2];
        oldrepres[pos2]=aux
        self.__repres=oldrepres
        
        return self
   
        
    def __str__(self):

        return "\nChromo: " + str(self.__repres) + " has fit: " + str(self.getFitness())
    
    def __repr__(self):
        return self.__str__()
    
    def __eq__(self, c):
        return self.__repres == c.__repres and self.__fitness == c.__fitness
