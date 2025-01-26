
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
    def inorder_traversal(self):
        if self.left:
            self.left.inorder_traversal()
        print(self.data,end=" ")
        if self.right:
            self.right.inorder_traversal()

    def preorder_traversal(self):
        print(self.data,end=" ")
        if self.left:
            self.left.preorder_traversal()
        if self.right:
            self.right.preorder_traversal()

    def posorder_traversal(self):
        if self.left:
            self.left.posorder_traversal()
        if self.right:
            self.right.posorder_traversal()
        print(self.data,end=" ")

    def find_ele(self,data):
        if data<self.data:
            if self.left is None:
                return 0
            else:
                return self.left.find_ele(data)
        elif data>self.data:
            if self.right is None:
                return 0
            else:
                return self.right.find_ele(data)
        else:
            return self.data

    def find_min(self):
        while self.left is not None:
            self=self.left
        return self.data

    def remove(self,data):
        if data <self.data:
            if self.left is not None:
                self.left=self.left.remove(data)
        elif data >self.data:
            if self.right is not None:
                self.right=self.right.remove(data)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is not None:
                return self.right
            elif self.right is not None:
                return self.left
            s=self.right.find_min()
            self.data=s
            self.right= self.right.remove(s)
        return self
    # display in reverse
    # def insert_end(self,data):
    #     if data:
    #         if self.right is not None:
    #             self.right=self.right.insert_end(data)
    #             self.right=Node(data)
    #         else:
    #             self=self.right
    #             self=Node(data)
    #     print(self.data,end=" ")


# a=[50,30,60,40,55,23,45,13]
# list=Node(a[-1])
# for i in range(len(a)-1,-1,-1):
#     list.insert_end(a[i])
# list.display_rev()
#list.remove(55)
#list.inorder_traversal()
# print()
# list.preorder_traversal()
# print()
# list.posorder_traversal()
# print()
