def hipify(value,n,i):
    largest=i

    l=2*i+1
    r=2*i+2
    if l<=n and arr[i]<arr[l]:
        largest=l
    if r<=n and arr[largest]<arr[r]:
        largest=r
    if i!=largest:
        value[largest],value[i]=value[i],value[largest]
        print(largest, i)
        print(value)
        hipify(value,n,largest)
    return  value



arr=[3, 2, 5, 7, 9, 1, 4, 6]
for i in range(len(arr)//2-1,-1,-1):
    print("loop",i)
    arr=hipify(arr,len(arr)-1, i)
    print(arr)

print("--------")
for i in range(len(arr)-1, 0, -1):
    arr[0], arr[i] = arr[i], arr[0]
    arr=hipify(arr, i-1,0)
print(arr)


