from collections import deque


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
    def height(self):
        if not self:
            return 0
        else:
            l=self.left.height() if self.left else 0
            r=self.right.height() if self.right else 0
        return max(l,r)+1
    def display(self,root):
        if not root:
            return None
        queue=deque([root])
        res=[]
        while queue:
            s=[]
            for i in range(len(queue)):
                n=queue.popleft()
                s.append(n.data)
                if n:
                    if n.left:
                        queue.append(n.left)
                    if n.right:
                        queue.append(n.right)
            res.append(s)
        return res

a=list(map(int,input().split()))
tree=Node(a[0])
for i in range(1,len(a)):
    tree.insert(a[i])
k=tree.height()
print(k)
l=tree.display(tree)

for i in l:
    print("left:",i[-1])
for i in l:
    print("right:",i[0])