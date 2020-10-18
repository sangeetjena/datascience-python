# this we want to build a graph to find the largest route followed by red bus app
from collections import defaultdict
path =[[1,2,3],
            [9 ,8,4],
            [ 11,7, 5],
           [12,13, 6]]

# to  create a direct acyclic graph
#we will build a dictionary and add keys as the edge aand add dependent edge
dag_path=defaultdict(list)
def build_dag():
    for i in range(len(path)):
        for j in range(len(path[i])):
            if (i!=0):
                if(abs(path[i-1][j]-path[i][j]) ==1):
                    dag_path[path[i][j]].append(path[i-1][j])
            if(j!=0):
                if (abs(path[ i  ][ j -1] - path[ i ][ j ]) == 1):
                    dag_path[path[ i ][ j ]].append(path[ i  ][ j-1 ])
            if (j != len(path[i])-1):
                if (abs(path[ i ][ j + 1 ] - path[ i ][ j ]) == 1):
                    dag_path[path[ i ][ j ]].append(path[ i ][ j +1 ])
            if (i != len(path)-1):
                if (abs(path[ i +1][ j  ] - path[ i ][ j ]) == 1):
                    dag_path[path[ i ][ j ]].append(path[ i +1][ j ])

build_dag()
for i in dag_path:
    print(dag_path[i])
    print("hello")

print(dag_path)