#Reverse a Linked List in groups of given size (Iterative Approach)

class linkedlist:
    #create new node
    def __init__(self,value):
        self.value=value
        self.next=None
     #insert node to the front of linked list
    def insert_node(self,head,node):
        node.next=head
    # reverse k nodes

#build a linked list
def linked_list_rev():
    arr=[8,7,6,5,4,3,2,1]
    head=None

    for i in range(0,len(arr)):
        node=linkedlist(arr[i])
        if (i==0):
            head=node
        else:
            node.next=head
            head=node

    # printing the linked list
    temp_head=head
    while(1==1):
        if (temp_head==None):
            break
        print(temp_head.value)
        temp_head=temp_head.next
    temp_head=head
    while(1==1):
        for i in range(0,3):
            if temp_head==None:
                break
            firest_node=temp_head
            temp

linked_list_rev()