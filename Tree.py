class tree:
    def __init__(self, val):
        self.value = val
        self.next = None
        self.prev = None
        self.parent = None


lst = [ 10,24,27,30,40,25,23,26,8,9,5,4,6,3 ]
count = 0
graph = None
head = None
for i in lst:
    graph = head
    count += 1
    if head == None:
        head = tree(i)
    else:
        while 1==1:
            if graph.value < i:
                if graph.next == None:
                    graph.next = tree(i)
                    graph.next.parent = graph
                    break
                else:
                    print(graph.value,"----->",i,count)
                    graph = graph.next
                    print(graph.value)
            else:
                if graph.prev == None:
                    graph.prev = tree(i)
                    graph.prev.parent = graph
                    break
                else:
                    print(graph.value, "----->",i,count)
                    graph = graph.prev
                    print(graph.value)
graph=head
tree=[]
count=0
print("tree reversal=====")
while not ((graph.next==None or graph.next.value==0) and (graph.prev==None or graph.prev.value==0) and graph.parent==None):
    count+=1
    if(graph.next!=None and graph.next.value!=0):
        graph=graph.next
    elif ((graph.next==None and graph.prev==None) or
          ( (graph.next==None or graph.next.value==0) and (graph.prev==None or graph.prev.value==0))):
            if graph.value!=-1:
                tree.append(graph.value)
                print(graph.value)
            graph.value=0
            graph=graph.parent
    else:
        tree.append(graph.value)
        print(graph.value)
        graph.value=-1
        graph=graph.prev
print(tree,count)