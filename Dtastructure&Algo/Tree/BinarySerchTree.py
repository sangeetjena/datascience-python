class node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
    def insert_to_tree(self,head,node):
        if (head.value>node.value):
            if (head.left==None):
                head.left=node
            else:
                self.insert_to_tree(head.left,node)
        if(head.value<node.value):
            if(head.right==None):
                head.right=node
            else:
                self.insert_to_tree(head.right,node)
    def traversal_tree(self,head):
        if  head==None:
            return
        self.traversal_tree(head.right)
        print(head.value)
        self.traversal_tree(head.left)


tree=node(10)
tree.insert_to_tree(tree,node(6))
tree.insert_to_tree(tree,node(20))
tree.insert_to_tree(tree,node(5))
tree.insert_to_tree(tree,node(30))
tree.insert_to_tree(tree,node(2))

tree.traversal_tree(tree)
