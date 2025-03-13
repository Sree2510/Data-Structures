class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def insert(self,data):
        if data<self.data:
            if self.left is None:
                self.left=Node(data)
            else:
                self.left.insert(data)
        else:
            if self.right is None:
                self.right=Node(data)
            else:
                self.right.insert(data)

    def find_min(self):
        value=self
        while value.left:
            value=value.left
        return value.data

    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.data,end=" ")
        if self.right:
            self.right.inorder()

    def remove(self,data):
        if data<self.data:
            if self.left is not None:
                self.left=self.left.remove(data)
        elif data>self.data:
            if self.right is not None:
                self.right=self.right.remove(data)
        else:
            if not self.right and not self.left:
                return None
            if not self.left:
                return self.right
            if not self.right:
                return self.left
            s = self.right.find_min()
            self.data=s
            self.right = self.right.remove(s)
        return self

a=list(map(int,input().split()))
list=Node(a[0])
for i in range(1,len(a)):
    list.insert(a[i])
list=list.remove(int(input()))
if list:
    list.inorder()