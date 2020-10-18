

class double_link_list:
    def __init__(self,value):
        self.value=value
        self.prev=None
        self.next=None

lst = ["sangeet",10,20,40,20,40]

head=None
for i in lst:
    obj = double_link_list(i)
    if(head!=None):
        head.next=obj
        obj.prev=head
    head=obj


while( head.prev != None):
    print(head.value)
    head=head.prev
print(head.value)



