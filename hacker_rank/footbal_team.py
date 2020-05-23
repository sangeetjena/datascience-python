import functools
a= [1,3,2,3,4]
b= [2,1,3,3,4]
cnt =0
for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        for k in range(0,len(b)):
            if (a[i]<a[j] and a[j]<b[k]):
                cnt=cnt+1
                print("one match is  ",a[i],a[j],b[k],cnt)

print("using function call in lambda expression")
lst = []
for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        x=(map(lambda x : [a[i],a[j],x],[x for x in b if a[i]<a[j] and a[j]<x]))
        for p in x:
            print(p)
        print("----")

