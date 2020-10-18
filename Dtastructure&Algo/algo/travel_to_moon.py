def journeyToMoon(n, astronaut):
    x=1
    for i in range(0,len(astronaut)):
        for y in astronaut[i]:
            for z in range(i+1,len(astronaut)):
                print(astronaut[z])
                print(astronaut)
                print("  ",y)
                if y in astronaut[z]:
                    print("matched")
                    astronaut[i]=list(set().union(astronaut[i],astronaut[z]))
                    astronaut[z]=[]
    print(astronaut)
    for i in astronaut:
        if len(i)>0:
            x=x*len(i)
    return x

x=[[0,1],[2,3],[0,4]]
print(journeyToMoon(1,x))
