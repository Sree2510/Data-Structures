class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
class DoubleLL:
    def __init__(self):
        self.head=None
    def f_display(self):
        value=self.head
        while value is not None:
            print(value.data,end=" ")
            value=value.next
    def insert_beginning(self,key):
        value=self.head
        ele=Node(key)
        value.prev=ele
        ele.next=value
        self.head=ele

    def insert_end(self,key):
        value=self.head
        new=Node(key)
        while value.next is not None:
            value=value.next
        value.next=new
        new.prev=value
    def insert_middle(self,key):
        value=self.head
        ele=Node(key)
        for i in range(1,3):
            value=value.next
        ele.next=value.next
        value.next.prev=ele
        value.next=ele
        ele.prev=value
    
    def remove(self):
        value=self.head
        for i in range(1,4):
            prev1=value
            value = value.next
        prev1.next=value.next
        value.next.prev=prev1
        value=None

a=[10,20,30,40,50]
list=DoubleLL()
for i in range(len(a)):
    value=Node(a[i])
    if i==0:
        list.head=value
        current= value
    else:
        current.next=value
        value.prev=current
        current=value
list.insert_beginning(5)
list.f_display()
print()
list.insert_end(60)
list.f_display()
print()
list.insert_middle(25)
list.f_display()
print()
list.remove()
list.f_display()