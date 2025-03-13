class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        self.cr=0
        self.cl=0

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
        lh=self.left.height() if self.left else 0
        rh=self.right.height() if self.right else 0
        return max(lh,rh)+1


    def lca(self,n1,n2):
        if n1<self.data and n2<self.data:
            if self.left:
                return self.left.lca(n1,n2)
        elif n1>self.data and n2>self.data:
            if self.right:
                return self.right.lca(n1,n2)
        elif n1<=self.data <=n2:
            return self.data

list=Node(6)
list.insert(2)
list.insert(8)
list.insert(0)
list.insert(4)
list.insert(7)
list.insert(9)
list.insert(3)
list.insert(5)
#print(list.height())
print(list.lca(2,4))

#
# a=int(input())
# b=eval(input())
# q=[_ for _ in b]
# c=int(input())
# d=int(input())
# e=int(input())
# sum=0
# k=0
# while q:
#     count,d=q.pop()
#     if k==count:
#         pass
#     else:
#         sum+=count
#     k=count
# print(sum)

"""3
[1,2],[2,1],[1,1]
2
3
3"""