class Node:
    def __init__(self,data,filename):
        self.data = data
        self.filename = filename
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:

    def get_height(self,node):
        if not node:
            return 0
        return node.height

    def get_balance(self,node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def right_rotate(self,y):
        x = y.left
        t2 = x.right
        x.right = y
        y.left = t2
        y.height = 1 + max(self.get_height(y.left),self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))

        return x

    def left_rotate(self,x):
        y = x.right
        t3 = y.left
        y.left = x
        x.right = t3
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))

        return y

    def insert(self,root,data,filename):
        if not root:
            return Node(data,filename)
        elif data < root.data:
            root.left = self.insert(root.left,data,filename)
        else:
            root.right = self.insert(root.right,data,filename)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        balance = self.get_balance(root)

        if balance > 1:
            if data < root.left.data:
                return self.right_rotate(root)
            else:
                root.left = self.left_rotate(root.left)
                return self.right_rotate(root)
        elif balance < -1:
            if data > root.right.data:
                return self.left_rotate(root)
            else:
                root.right = self.right_rotate(root.right)
                return self.left_rotate(root)

        return root

    def preorder(self,root):
        if root:
            self.preorder(root.left)
            print(root.filename,root.data)
            self.preorder(root.right)

# import re
#
# def find(s):
#     match = re.search(r'\d',s)
#     return int(match.group()) if match else 0

def find(s):
    for i in s:
        if i.isdigit():
            return int(i)
    return 0

AVL = AVLTree()
root=None
arr = ["File4.txt","File5.txt","File2.txt","File1.txt","File3.txt"]
for i in arr:
    k = find(i)
    print(k)
    root = AVL.insert(root,k,i)

AVL.preorder(root)