arr= [1,2,3,4,5,6]

len= len(arr)-1
print(arr)
for i in range(len):
    if (abs(i-(len-i))==1):
        x= arr[i]
        arr[i]=arr[len-i]
        arr[len-i]=x
        break
    x = arr[ i ]
    arr[ i ] = arr[ len - i ]
    arr[ len - i ] = x

print(arr)
