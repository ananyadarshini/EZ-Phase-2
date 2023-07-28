class Node:
    def __init__(self,data):
        self.previous=None
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
    def delete_position(self,pos):
        previous=self.head
        temp=self.head.next
        for i in range(1,pos-1):
            temp=temp.next
            previous=previous.next
        prev.next=temp.next
        temp.next=None
        temp.prev=prev
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
dl.delete_position(2)
dl.display()

