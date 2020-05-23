class node:
    def __init__(self, val):
        self.value = val
        self.next = None


class linked_list_header:
    def __init__(self):
        self.headnode = None

lst = [6,10,11,90,50,60,45,1]

node1 = node(3)
node2 = node(4)
node3 = node(5)
node4 = node(9)
head = linked_list_header()
head.headnode = node(2)
head.headnode.next = node1
node1.next = node2
node2.next = node3
node3.next = node4
nd = None
lp = iter(range(1, 4))
for i in lst:
    new_node= node(i)
    nd = head.headnode
    while 1==1:
        if nd.value>i:
            new_node.next=nd
            head.headnode=new_node
            print("1st insert")
            break
        if nd.next != None:
            if (i>nd.value and i<nd.next.value):
                new_node.next=nd.next
                nd.next=new_node
                print("enter in between",i)
                break
            else:
                nd=nd.next
        else:
            nd.next=new_node
            print("enter last",i)
            break
nd=head.headnode
while 1==1:
    if nd.next==None:
        print(nd.value)
        break
    print(nd.value)
    nd=nd.next