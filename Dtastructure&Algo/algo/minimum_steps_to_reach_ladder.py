steps={1:2,
       2:1,
       3:3,
       4:4,
       5:3,
       6:3,
       7:1,
       8:1,
       9:2,
       10:1,
       11:0}

curr=1
end=1
mx=0
maxsteps=0
while (curr <= max(steps.keys())):
    print(curr)
    mx = 0
    next=0
    if (steps[curr] == 0):
        break
    for i in range(curr,curr+steps[curr]+1):
        print("   ", i,"   ",steps[i]+i )
        if mx<(steps[i]+i):
            mx=steps[i]+i
            next=i
    maxsteps = maxsteps + 1
    if next==curr:
        curr=mx
    else:
        curr=next


print(maxsteps)
