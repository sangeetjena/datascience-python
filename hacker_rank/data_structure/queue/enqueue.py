x = []
class queue:
    def __init__(self):
        x.clear()
    def equeue(self,element,que):
        que.append(element)
        return que
    def deque(self,que):
        return que[1:]
q = queue()
x= q.equeue(2,x)
x=q.equeue(3,x)
x=q.deque(x)
print(x)
