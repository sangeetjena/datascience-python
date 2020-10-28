import sys
def mean_weight(weight_arr,travelled_arr):
    min = sys.maxsize
    ind=0
    for i in range(0,len(weight_arr)):
        if min>weight_arr[i] and  travelled_arr[i]!=1:
            min=weight_arr[i]
            ind=i
    return ind
def djistra(graph,start):
    travelled=[0 for i in range(0,len(graph))]
    weight_vertex=[sys.maxsize for i in range(0,len(graph))]
    route=[0 for i in range(len(graph))]
    weight_vertex[start]=0
    for i in graph:
        min_v=mean_weight(weight_vertex,travelled)
        travelled[min_v]=1
        for i in range(0,len(graph)):
            #child vertex shoud have connection to the indexed verted , it should not have traversed ,
            #chose min weight of its child vertex.
            if (graph[min_v][i]!=0
                    and weight_vertex[i] not in travelled
                    and weight_vertex[i]>weight_vertex[min_v]+graph[min_v][i]):
                #weight of node = weight of its parent + connection weight
                weight_vertex[i]=weight_vertex[min_v] + graph[min_v][i]
                route[i]=min_v
    print(route)
    return weight_vertex
gf=[[0,2,1,0,0],
    [0,0,0,1,0],
    [0,0,0,4,0],
    [0,0,0,0,2],
    [0,0,0,0,0]]
res=djistra(gf,0)

for i in range(len(res)):
    print(i,"weight ",res[i])


