class node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
def is_operator(ch):
    if (ch=='+' or ch=='-' or ch=='/' or ch=='*'):
        return True

def post_order(t):
    if t !=None:
        post_order(t.right)
        print(t.val)
        post_order(t.left)
def pre_order(t):
    if t !=None:
        post_order(t.right)
        post_order(t.left)
        print(t.val)

def expression_tree(lst):
    stack=[]
    t=None
    for i in lst:
        if is_operator(i)!=True:
            stack.append(node(i))
        else:
            t=node(i)
            t1=stack.pop()
            t2=stack.pop()
            t.right=t1
            t.left=t2
            stack.append(t)
    post_order(t)
    pre_order(t)

lst=['a','b','+','e','f','*','g','*','-']
expression_tree(lst)