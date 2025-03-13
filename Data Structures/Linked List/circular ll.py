class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Circular:
    def __init__(self):
        self.head=None
    def solve(self,b):
        value=self.head
        while value.next!=value :
            current=None
            for i in range(b-1):
                current=value
                value=value.next
            current.next=value.next
            value=None
            value=current.next
        return value.data

a=16
b=4
list=Circular()
for i in range(1,a+1):
    value=Node(i)
    if i==1:
        list.head=value
        current=value
    else:
        current.next=value
        current=value
current.next=list.head
print(list.solve(b))