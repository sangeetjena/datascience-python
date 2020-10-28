#logic behind is that it will keep deviding all the elements and up to reach the single elements
# the n keep forming sorted arrays and merge two to create one sorted array and that again
#sorted with others left.

def merge_sort(value):
    if len(value)>1:
        mid= len(value)//2
        left=value[:mid]
        right=value[mid:]
        left=merge_sort(left)
        right=merge_sort(right)
        value=[]
        while len(left)>0 and len(right)>0:
            if left[0]>right[0]:
                value.append(left[0])
                del left[0]
            else:
                value.append(right[0])
                del right[0]
        for i in left:
            value.append(i)
        for i in right:
            value.append(i)
    return value
lst=[1,5,4,3]
res=merge_sort(lst)
print(res)