str="geegsforgeegs"
tmp=[]
maxstr=[]
max=0
end=0

while end<len(str):
    if (str[end] in tmp):
        del tmp[0]
    else:
        tmp.append(str[end])
        if max<len(tmp):
            max=len(tmp)
            maxstr=tmp.copy()
        end=end+1
print(maxstr)
print(max)
