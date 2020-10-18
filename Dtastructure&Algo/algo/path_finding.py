#longest path

path={1:[2,3],2:[4,6],3:[],4:[5],5:[9],9:[],6:[7],7:[]}

max=0
arr=[]
def line_draw(source,cnt):
    global max
    for v in path[source]:
            line_draw(v,cnt+1)
            if cnt+1>max:
                max=cnt+1
            print(v)
    return max
print(line_draw(1,0))
