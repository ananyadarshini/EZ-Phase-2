class Node:
    def __init__(self,data):
        self.previous=None
        self.data=data
        self.next=None

class DLL:
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
    def deleteatbegin(self):
        temp=self.head
        self.head=temp.next
        temp.next.previous=None
        temp.next=None
Node_1=Node("Rishika")
Node_2=Node("asha")
Node_3=Node("anu")
dl=DLL()
dl.head=Node_1
Node_1.next=Node_2
Node_2.previous=Node_1
Node_2.next=Node_3
Node_3.previous=Node_2
dl.display()
print()
dl.deleteatbegin()
dl.display()

