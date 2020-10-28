#bellman fort algorithm is sweetable for the negetive weighted greaph.
#but if there is a cycle then this fail
import sys
def bellman_fort(graph,start):
    vertex=[sys.maxsize for i in range(len(graph))]
    vertex[start]=0
    for i in range(len(vertex)):
        for y in range(len((vertex))):
            if (vertex[y]!=sys.maxsize):
                for z in range(len(vertex)):
                    if(graph[y][z]!=0):
                        if vertex[z]>vertex[y]+graph[y][z]:
                            vertex[z]=vertex[y]+graph[y][z]
    print(vertex)
gf=[[0,2,1,0,0],
    [0,0,0,1,0],
    [0,0,0,4,0],
    [0,0,0,0,2],
    [0,0,0,0,0]]
bellman_fort(gf,0)