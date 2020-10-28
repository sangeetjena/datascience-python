#this algorithm is to find minimum spanning tree in the given graph.
#this will find the minimum sub tree in the graph
#but distance from any vertex to the other might not be the optimal path

import sys
def find_min(vertex,travelled):
    min=sys.maxsize
    min_index=0
    for i in range(len(vertex)):
        if min>vertex[i] and i not in travelled:
            min=vertex[i]
            min_index=i
    return min_index

def prims(graph):
    travelled=[]
    vertex=[sys.maxsize for i in graph]
    parent=[-1 for i in graph]
    vertex[0]=0
    for i in vertex:
        min_v=find_min(vertex,travelled)
        print(min_v)
        travelled.append(min_v)
        for i in range(len(vertex)):
            if graph[min_v][i]!=0 and vertex[i]>graph[min_v][i]:
                vertex[i]=graph[min_v][i]
                parent[i]=min_v
    print(travelled)
    print(vertex)
    return parent
graph = [ [0, 2, 0, 6, 0],
            [2, 0, 3, 8, 5],
            [0, 3, 0, 0, 7],
            [6, 8, 0, 0, 9],
            [0, 5, 7, 9, 0]]
print(prims(graph))
