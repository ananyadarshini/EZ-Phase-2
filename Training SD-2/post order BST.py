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
    def post_order(self):
        if self.l_child:
            self.l_child.post_order()
        if self.r_child:
            self.r_child.post_order()
        print(self.key,end="")
list=[1,2,4,5,7,4,8,3,4,5]
obj=BST(5)
for i in list:
    obj.insert_node(i)
obj.post_order()
    



                
            
