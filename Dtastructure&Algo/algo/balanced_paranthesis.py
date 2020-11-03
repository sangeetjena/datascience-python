#lst=['[','(',')',']','{','}','{','[','(',')','(',')',']','(',')','}']
lst=['[','(',']',')']
char_dict={"]":'[' , ")":'(',"}":'{'}
ind=0
while len(lst)>0:
    if ind==1:
        break
    ind=1
    for i in range(1,len(lst)):
        if(lst[0] in char_dict.keys()):
            break
        if lst[0]==char_dict.get(lst[i]) and len(lst[0:i+1])%2==0:
            del lst[i]
            del lst[0]
            print(lst)
            ind=0
            break
if ind==0:
    print("matched")
else:
    print("not matched")
