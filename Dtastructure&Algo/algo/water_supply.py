"""Given N cities that are connected using N-1 roads. Between Cities [i, i+1], there exists an edge for all i from 1 to N-1.
The task is to set up a connection for water supply. Set the water supply in one city and water gets transported from it to other cities using road transport. Certain cities are blocked which means that water cannot pass through that particular city. Determine the maximum number of cities to which water can be supplied.
"""


path={1:[2,3],2:[4,6],3:[],4:[5],5:[],6:[7],7:[]}

supply=[]
block=[2]
cnt=0
def line_draw(source):
    global cnt
    for v in path[source]:
        if(v in block):
            continue
        else:
            line_draw(v)
            if v not in supply:
                cnt=cnt+1
                supply.append(v)
    return
line_draw(1)
print(supply)




line_draw(1)

