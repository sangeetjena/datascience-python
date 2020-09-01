class Bst:
    def __init__(self,node):
        self.node = node
        self.left = None
        self.right= None
    def insert_leaf_node(self,head,node1):
        if(head.node>node1.node):
            if (head.left ==None):
                head.left=node1
            else:
                self.insert_leaf_node(head.left,node1)
        if(head.node<node1.node):
            if(head.right==None):
                head.right=node1
            else:
                self.insert_leaf_node(head.right,node1)
        if(head.node==node1.node or head.node ==None):
            head.node=node1.node

head = Bst(15)
nd = Bst(12)
head.insert_leaf_node(head,nd)
nd1 = Bst(20)
head.insert_leaf_node(head,nd1)

