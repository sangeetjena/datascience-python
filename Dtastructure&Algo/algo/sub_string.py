s1=[1,3,5,6,7,4,8,2,14,13,12]
s2=[3,4,15]
hash=[[] for i in range(9)]
for i in s1:
    hash[i%10].append(i)
all_exists=1
for i in s2:
    x=0
    for j in hash[i%10]:
        if i==j:
            x=1
            break
    if x==0:
        all_exists=0
        break
if all_exists==0:
    print("element not found")
else:
    print("found")
print(hash)