class Node:
    def __init__(self,data):
        self.data=data
        self.l_child=None
        self.r_child=None
class Tree_ds:
    def __init__(self):
        self.root=None
obj=Tree_ds
node_1=Node(10)
node_2=Node(20)
node_3=Node(30)
print(node_1.data)
