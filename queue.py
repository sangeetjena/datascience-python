class queue:
    def __init__(self,value):
        self.value=value
        self.prev=None
        self.next=None


lst= [1,2,4,5,7,8]

head=None
tail=None

for i in lst:
    obj=queue(i)
    if(tail==None):
        head=obj
        tail=obj
    else:
        tail.next=obj
        obj.prev=tail
    tail=obj

print("queue")
while (1):
    print(tail.value)
    if (tail.prev == None):
        break

    tail=tail.prev



print("stack")
while(1):
    print(head.value)
    if (head.next == None):
        break

    head=head.next
