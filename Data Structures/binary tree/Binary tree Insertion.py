# # from collections import deque
# # class Node:
# #     def __init__(self,data):
# #         self.data=data
# #         self.left=None
# #         self.right=None
# #
# #     def display(self,root):
# #         if not root:
# #             return None
# #         queue=deque([root])
# #         res=[]
# #         while queue:
# #             s=[]
# #             for i in range(len(queue)):
# #                 n=queue.popleft()
# #                 s.append(n.data)
# #                 if n:
# #                     if n.left:
# #                         queue.append(n.left)
# #                     if n.right:
# #                         queue.append(n.right)
# #             res.append(s)
# #         return res
# # def insert(arr,root):
# #     queue=[root]
# #     i=1
# #     while i<len(arr):
# #         c=queue.pop(0)
# #         if c:
# #             if arr[i] and arr[i]!=-1:
# #                 c.left=Node(arr[i])
# #                 queue.append(c.left)
# #             i+=1
# #             if i<len(arr) and arr[i]!=-1:
# #                 c.right=Node(arr[i])
# #                 queue.append(c.right)
# #             i+=1
# #     return root
# #
# # a=list(map(int,input().split()))
# # root=Node(a[0])
# # k=insert(a,root)
# # l=root.display(k)
# # print(l)
# # if l:
# #     print("right:",end=" ")
# #     for i in l:
# #         print(i[-1],end=" ")
# #     print("\nleft:",end=" ")
# #     for i in l:
# #         print(i[0],end=" ")
#
from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def display(root):
    if not root:
        return None
    queue = deque([root])
    ans = []
    while queue:
        s=[]
        for i in range(len(queue)):
            k = queue.popleft()
            s.append(k.data)
            if k:
                if k.left:
                    queue.append(k.left)
                if k.right:
                    queue.append(k.right)
                if s:
                    ans.append(s)
    return ans


def insert(arr, root):
    queue = [root]
    i = 1
    while i < len(arr):
        k = queue.pop(0)
        if k:
            if arr[i] and arr[i] != -1:
                k.left = Node(arr[i])
                queue.append(k.left)
            i += 1
            if i < len(arr) and arr[i] != -1:
                k.right = Node(arr[i])
                queue.append(k.right)
            i += 1
    return root
# def insert(root,data):
#     if not root:
#         return Node(data)
#     queue=[root]
#     while queue:
#         k=queue.pop(0)
#         if not k.left:
#             k.left=Node(data)
#             break
#         elif k.left.data!=-1:
#             queue.append(k.left)
#         if not k.right:
#             k.right=Node(data)
#             break
#         elif k.right.data!=-1:
#             queue.append(k.right)
#     return root

a = list(map(int, input().split()))
root = Node(a[0])
k = insert(a, root)
# x=None
# for i in a:
#     x=insert(x,i)
l = display(k)
for i in l:
    print(i[0],end=" ")
print(l)
#
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
#
#
# def insert(root, data):
#     if root is None:
#         return Node(data)
#     queue = [root]
#     while queue:
#         cur = queue.pop(0)
#         if cur.left is None:
#             cur.left = Node(data)
#             break
#         elif cur.left.data != -1:
#             queue.append(cur.left)
#         if cur.right is None:
#             cur.right = Node(data)
#             break
#         elif cur.right.data != -1:
#             queue.append(cur.right)
#     return root
#
#
# def leftview(root, height, res):
#     if root is None or root.data == -1:
#         return
#     if height >= len(res):
#         res.append(root.data)
#     leftview(root.left, height + 1, res)
#     leftview(root.right, height + 1, res)
#
#
# l = list(map(int,input().split()))
# root = None
# for i in l:
#     root = insert(root, i)
# res = []
# leftview(root, 0, res)
# print(res)
