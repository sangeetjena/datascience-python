lst=[[10,9,4,1],[8,5],[3,2]]

def sort_merge(arr):
    mid=len(arr)//2
    if len(arr)==1:
        return arr
    l=sort_merge(arr[:mid])
    r=sort_merge(arr[mid:])
    tmp_lst=[]
    while len(l)>0 and len(r)>0:
        if l[0]>r[0]:
            tmp_lst.append(l[0])
            del l[0]
        else:
            tmp_lst.append((r[0]))
            del r[0]
    for i in l:
        tmp_lst.append(i)
    for y in r:
        tmp_lst.append(y)
    return tmp_lst

final_big=[]
n=3
for i in lst:
    for y in i:
        if len(final_big)==0 :
            final_big.append(y)
            continue
        if y < final_big[ len(final_big) - 1 ] and len(final_big)>2:
            continue
        final_big.append(y)
        final_big=sort_merge(final_big)
        if (len(final_big)>3):
            del final_big[len(final_big)-1]

print(final_big)

