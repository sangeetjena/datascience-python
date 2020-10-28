def pivot(value,low,high):
    i=low-1
    pivot=value[high]
    for j in range(low,high):
        if value[j]<value[high]:
            i=i+1
            value[i],value[j]=value[j],value[i]
    print(i,high)
    value[i+1],value[high]=value[high],value[i+1]
    return (i+1)


def quick_sort(value,low,high):
    print(value)
    print(low,high)
    if low<high:
        partition=pivot(value,low,high)
        quick_sort(value,low,partition-1)
        quick_sort(value,partition+1,high)
    return value

arr=[3,6,5,7,8,1]
print(quick_sort(arr,0,len(arr)-1))

