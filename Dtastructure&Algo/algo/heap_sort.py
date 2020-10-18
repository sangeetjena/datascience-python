import math

def hipify(hp,i=0):
    if len(hp)==1:
        return hp
    j=math.floor(i/2)
    if j!=0 and hp[i-1]>hp[j-1]:
        hp[ j - 1 ]=hp[j-1] + hp[i-1]
        hp[ i - 1 ]= hp[ j - 1 ] - hp[ i - 1 ]
        hp[ j - 1 ] = hp[ j - 1 ] - hp[ i - 1 ]
        hipify(hp,j)
    else:
        return hp
    return hp


def sort_heap(heap,end):
    if end<=0:
        return heap
    print(end)
    heap[0]=heap[end]+heap[0]
    heap[end]=heap[0]-heap[end]
    heap[0]=heap[0]-heap[end]
    i=0
    while i<end-1:
        if i+2>end-1:
            if heap[i]<heap[i+1]:
                heap[i]=heap[i]+heap[i+1]
                heap[i+1]= heap[i]-heap[i+1]
                heap[i]=heap[i]-heap[i+1]
                i=i+1
            else:
                break
        else:
            if i<end-2:
                if heap[i+1]>heap[i+2]:
                    if heap[i]<heap[i+1]:
                        heap[ i ] = heap[ i ] + heap[ i + 1 ]
                        heap[ i + 1 ] = heap[ i ] - heap[ i + 1 ]
                        heap[ i ] = heap[ i ] - heap[ i + 1 ]
                        i = i + 1
                        continue
                    else:
                        break
                else:
                    if heap[i]<heap[i+2]:
                        heap[ i ] = heap[ i ] + heap[ i + 2 ]
                        heap[ i + 2 ] = heap[ i ] - heap[ i + 2 ]
                        heap[ i ] = heap[ i ] - heap[ i + 2 ]
                        i = i + 2
                        continue
                    else:
                        break
    sort_heap(heap,end-1)
    return heap



y=[]
x=[3, 2, 5, 7, 9, 1, 4, 6]
for i in x:
    y.append(i)
    y=hipify(y,len(y)-1)
print(y)
p=sort_heap(y,len(y)-1)

print(p)

