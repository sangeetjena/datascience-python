
class linked_list:
    def __init__(self,next,node):
        self.next= next
        self.node= node

head = linked_list(None,None)
head.node=10

x= linked_list(None,None)
x.node=11

head.next=x

print(head.node)
print(head.next.node)