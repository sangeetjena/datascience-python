class btree:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
    def insert(self,node, head1):
        head=head1

        if head==None:
            head=node
            print("1st node")
            return head
        while head!=None:
            if node.val>head.val and head.right==None:
                head.right=node
                return
            elif  (node.val>head.val and head.right!=None):
                head=head.right
                print("right ")
            elif (node.val<head.val and head.left==None):
                head.left=node
                return
            elif (node.val<head.val and head.left!=None):
                head=head.left
                print("left ")
    def traversal_tree(self,head):
        if  head==None:
            return
        self.traversal_tree(head.right)
        print(head.val)
        self.traversal_tree(head.left)

head=btree(20)
head.insert(btree(10),head)
head.insert(btree(1),head)
head.insert(btree(6),head)
head.insert(btree(30),head)
head.insert(btree(60),head)
head.insert(btree(3),head)
head.insert(btree(9),head)

head.traversal_tree(head)



