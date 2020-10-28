#find the  sum of list * elemet in the nested list

lst=[1,2,3,
     [1,2,3],
     [1,2,[1,2]]]


def find_sum(lst):
    sum=0
    cnt=0
    for i in lst:
        if type(i)==list:
            sum1,cnt1=find_sum(i)
            sum=sum + (sum1*cnt1)
            cnt=cnt+1
        else:
            sum=sum+i
            cnt=cnt+1
    print(sum,"---",cnt)
    return sum,cnt

sum=0
cnt=0
for i in lst:
    if(type(i)==int):
        sum=sum+i
        cnt=cnt+1
        print("accumulated sum ",sum)
    else:
        print("found list in list")
        sum1,cnt1=find_sum(i)
        sum=sum+(sum1*cnt1)
        cnt=cnt+1
final_sum=sum*cnt
print(final_sum)
