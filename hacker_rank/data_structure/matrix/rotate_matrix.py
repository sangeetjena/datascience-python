import copy
arr = [[1,2,3,4,5,6],
            [7,8,9,10,11,12],
       [13,14,15,16,17,18],
       [19,20,21,22,23,24],
       [25,26,27,28,29,30],
       [31,32,33,34,35,36]]
# results

[[7, 1, 2, 3, 4, 5],
 [13, 14, 8, 9, 10, 6],
 [19, 20, 21, 15, 11, 12],
 [25, 26, 22, 16, 17, 18],
 [31, 27, 28, 29, 23, 24],
 [32, 33, 34, 35, 36, 30]]
print(arr)
temparr = []
rotate_arr  = copy.deepcopy(arr)
for x in range(0,round(len(arr[0])/2)):
    xstart =x
    xbottom= len(arr[0])-1-x
    ystart=x
    yright =len(arr[0])-1-x
    for i in range(x,yright):
        temparr.append(arr[x][i])
        rotate_arr[x][i+1]=arr[x][i]
    for i in range(x,yright):
        temparr.append((arr[i][yright]))
        rotate_arr[i+1][yright]=arr[i][yright]
    for i in reversed(range(x,yright+1)):
        if(i!=x):
            temparr.append(arr[yright][i])
            rotate_arr[yright][i-1]=arr[yright][i]
    for i in reversed(range(x,yright+1)):
        if(i!=x):
            temparr.append((arr[ i ][ xstart ]))
            rotate_arr[i-1][xstart]=arr[ i ][ xstart ]
    print(temparr)
    temparr=[]

print(rotate_arr)

[[7, 1, 2, 3, 4, 5],
 [13, 14, 8, 9, 10, 6],
 [19, 20, 21, 15, 11, 12],
 [25, 26, 22, 16, 17, 18],
 [31, 27, 28, 29, 23, 24],
 [32, 33, 34, 35, 36, 30]]



