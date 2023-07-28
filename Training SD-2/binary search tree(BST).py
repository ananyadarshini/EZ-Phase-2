class BST:
    def __init__(self,key):
        self.key=key
        self.l_child=None
        self.r_child=None
    def insert_node(self,data):
        if self.key is None:
            return
        if self.key==data:
            return
        if self.key>data:
            if self.l_child:
                self.l_child.insert_node(data)
            else:
                self.l_child=BST(data)
        else:
            if self.r_child:
                self.r_child.insert_node(data)
            else:
                self.r_child=BST(data)
obj=BST(45)
obj.insert_node(30)
obj.insert_node(60)
obj.insert_node(50)
obj.insert_node(20)
obj.insert_node(70)
obj.insert_node(43)
obj.insert_node(56)
obj.insert_node(89)
obj.insert_node(12)
obj.insert_node(67)
print(obj.key)
print(obj.l_child.key)
print(obj.r_child.key)


                
            
