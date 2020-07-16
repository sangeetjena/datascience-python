def arrayManipulation(n, queries):
    temp_array=[0 for x in range(0,n+1) ]

    max = -10000
    for x in queries:

        if x.__len__()==3:
            for i in range(x[0],x[1]+1):
                temp_array[i] = temp_array[i]+x[2]
                if(max<temp_array[i]):
                    max=temp_array[i]
            print(temp_array)
    return max

queries =[[2, 6, 8],
[3, 5, 7],
[1, 8, 1],
[5 ,9 ,15]]
print(arrayManipulation(10, queries))