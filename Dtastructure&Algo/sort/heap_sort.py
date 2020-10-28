def hipify(value,n,i):
    largest=i
    l=2*i+1
    r=2*i+2

    if l<=n and value[i]<value[l]:
       largest = l
    if r<=n and value[largest]<value[r]:
       largest=r
    if i!=largest:
       value[i],value[largest]=value[largest],value[i]
       hipify(value,n,largest)
    return value


arr=[3, 11,2, 12,5, 7, 9,10, 1, 4, 6]
for i in range(len(arr)//2-1,-1,-1):
    hipify(arr,len(arr)-1,i)
print(arr)
for i in range(len(arr)-1,0,-1):
    arr[0],arr[i]=arr[i],arr[0]
    hipify(arr,i-1,0)
print(arr)


