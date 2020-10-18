arr=[1,5,6,3,8,2,7,4]

val =8

for i in range(0,len(arr)):
    for j in range(i,len(arr)):
        if(arr[i]>arr[j]):
           arr[i]=int(arr[i]*arr[j])
           arr[j]=int(arr[i]/arr[j])
           arr[i]=int(arr[i]/arr[j])
print(arr)
upper = len(arr)
lower = 0
mid = int(abs((0 + len(arr)) / 2))
while(1==1):
    if val>arr[mid]:
        lower=mid
        mid=int(abs((lower+upper)/2))
    elif val<arr[mid]:
        upper=mid
        mid=int(abs((lower+mid)/2))
    elif (val==arr[mid]):
        print("found - "+ str(mid))
        break














