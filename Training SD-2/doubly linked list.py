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
            print("doubly linked list is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"->",end=" ")
                temp=temp.next
obj=DLL()
n=Node('Ananya')
obj.head=n
n1=Node('anuhya')
obj.head.next=n1
n2=Node('Rishika')
n1.next=n2
n3=Node('Asha')
n2.next=n3
obj.display()
