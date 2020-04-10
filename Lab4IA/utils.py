from random import randint
def readData(filename):
    f = open(filename,"r")
    n = int(f.readline().strip())
    matrix = []
    for i in range(n):
        line = f.readline().strip()
        args = line.split(",")
        args=[int(val) for val in args]
        matrix.append(args);

    net = {}
    
    net["noNodes"] = n
    net["matrix"] = matrix
    return net

net=readData("C:\\Users\\Patcas\\source\\repos\\Lab4IA\\Lab4IA\\data.txt");

def generateARandomPermutation(n):
    perm=[]
    for i in range(0,n):
        nr=randint(0,n-1)
        while (nr in perm):
            nr=randint(0,n-1)
        perm.append(nr)
    return perm





