from functools import reduce
import  datetime


str= "ssd,df,df,fgf,fg"
arr = str.split(",")

((lambda a:print(a),arr))
print(arr[len(arr)-1])


print()
number,rotation = input().split(" ")                  # Reading input from STDIN
arr = input().split(" ")
for i in range(0,int(rotation)):
    element=arr[0]
    arr.remove(arr[0])
    arr.append(element)
str = (reduce(lambda  a: a+' ',arr))
print(str)


num  = input()
a=[]
for i in range(1,round(int(num)/2)+1):
    a.append(i)
print(a)

for i in range(2,round(int(num)/2)+1):
    sum=0
    for y in range(0,len(a)-i+1):
        sum =reduce(lambda a,b:a+b,a[y:y+i])
        if sum==int(num):
            print(a[y:y+i])




lst = [7, 7, 8, 8, 9, 1, 1, 4, 2, 2, 1, 3, 5]
x = iter(range(1, len(lst)))
for i in x:
    if(lst[i] == lst[i-1]):
        next(x, None)
    else:
        print(lst[i - 1])

