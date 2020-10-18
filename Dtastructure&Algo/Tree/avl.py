"""
avl tree is a tree whose any node from its edgenode should not have relative distace more than 1
(left branch - right branch)<=1
in order to adjust we run ll lr, rr, ll rotation to make a branch balanced
"""
class node:
    def __init__(self,val):
        self.val=val
        self.right=None
        self.left=None
        self.height=1
class tree:
    def root_height(self,head):
        # if root is null to handle that
        if head==None:
            return 0
        return head.height
    def balance(self,head):
        if root==None:
            return 0
        return self.root_height(head.left)-self.root_height(head.right)
    def insert(self,head,value):
        print("insert funtion")
        if head==None:
            return node(value)
        if value>head.val:
            #here at the time of going to right of node i am storing right address again , i.e because
            # after insertion i will connect the tree re balance again so the address need to ebe recapture.
            head.right=self.insert(head.right,value)
        elif value<head.val:
            # this is hight reference of the current root for its previous root.
            head.left=self.insert(head.left,value)
        head.height=1+max(self.root_height(head.left),self.root_height(head.right))
        balance_factor = self.balance(head)
        if balance_factor>1 and value>head.left.val:
            head.left=self.left_rotation(head.left)
            return self.right_rotation(head)
        if balance_factor>1 and value<head.left.val:
            return self.right_rotation(head)
        if balance_factor<1 and value>head.right.val:
            return self.left_roatation(head)
        if balance_factor<1 and value<head.right.val:
            head.right=self.right_rotation(head.right)
            return self.left_rotation(head)
        return head
    def right_rotation(self,z):
        y=z.left
        t3=y.right
        y.right=z
        z.left=t3
        # here only z and y changed their hieight not its rest of the child nodes
        # so only z and y height need to be recalculated.
        z.height=1+max(self.root_height(z.left),self.root_height(z.right))
        y.height=1+max(self.root_height(y.left),self.root_height(y.right))
        # after rebalancing the present edge need to be resend to hold by it previous node
        return y
    def left_rotation(self,z):
        y=z.right
        t2=y.left
        y.left=z
        z.right = t2

        z.heigt=1+max(self.root_height(z.left),self.root_height(z.right))
        y.height=1+max(self.root_height(y.left),self.root_height(y.right))
        return y
    def print_tree(self,root):
        print("print function")
        if root==None:
            return
        self.print_tree(root.left)
        print(root.val,root.height)
        self.print_tree(root.right)

tree=tree()
root=None
root=tree.insert(root,3)
root=tree.insert(root,6)
root=tree.insert(root,5)
root=tree.insert(root,8)
root=tree.insert(root,7)
tree.print_tree(root)








