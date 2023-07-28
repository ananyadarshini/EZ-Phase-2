class Node:
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.next=None
class Dll:
    def __init__(self):
        self.head=None
    def display(self):
        if self.head is None:
            print("double ll  is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"-->",end="")
                temp=temp.next
    def insert_position(self,pos,data):
        new_node=Node(data)
        temp=self.head
        for i in range(1,pos-1):
            temp=temp.next
        new_node.prev=temp
        new_node.next=temp.next
        temp.next.prev=new_node
        temp.next=new_node
Node_1=Node("Rishika")
Node_2=Node("asha")
Node_3=Node("anu")
dl=Dll()
dl.head=Node_1
Node_1.next=Node_2
Node_2.previous=Node_1
Node_2.next=Node_3
Node_3.previous=Node_2
dl.display()
print()
dl.insert_position(4,"Anuhya")
dl.display()
