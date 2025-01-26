# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.left=None
#         self.right=None
#     def built_tree(self,a,b):
#         if not a or not b:
#             return None
#         root_val=a[0]
#         root= Node(root_val)
#         root_index = b.index(root_val)
#
#         left_b=b[:root_index]
#         right_b=b[root_index+1:]
#
#         left_a=a[1:1+len(left_b)]
#         right_a=a[1+len(left_b):]
#
#         if left_a:
#             root.left=self.built_tree(left_a,left_b)
#         if right_a:
#             root.right=self.built_tree(right_a,right_b)
#         return root
#     def level_tree(self):
#         queue=[(self,True)]
#         result=[]
#         while queue:
#             level_size=len(queue)
#             for i in range(level_size):
#                 current,is_last=queue.pop(0)
#                 if current:
#                     result.append(current.data)
#                     queue.append((current.left, i == level_size - 1 and (current.left or current.right)))
#                     queue.append((current.right, i == level_size - 1 and (current.left or current.right)))
#                 else:
#                     result.append(None)
#                     if is_last:
#                         break
#         return result
# a=[3,2,1,5,4]
# b=[1,2,3,4,5]
# root=Node(a[0])
# tree=root.built_tree(a,b)
# print(tree.level_tree())


class Node:
    def __init__(self,data=0):
        self.data=data
        self.left=None
        self.right=None


    def build_tree(self,preorder,inorder):
        if not preorder or not inorder:
            return None
        root_value=preorder[0]
        root_index=inorder.index(root_value)

        inorder_left=inorder[:root_index]
        inorder_right=inorder[root_index+1:]
        preorder_left=preorder[1:1+len(inorder_left)]
        preorder_right=preorder[1+len(inorder_left):]
        root=Node(root_value)
        root.left= self.build_tree(preorder_left,inorder_left)
        root.right= self.build_tree(preorder_right,inorder_right)
        return root

def maximum_length(root):
    if root is None:
        return 0
    else:
        left_depth=  maximum_length(root.left)
        right_depth= maximum_length(root.right)
    return max(left_depth,right_depth)+1

def level_traversal(root,l):
    if not root:
        return ["null"]
    queue=[(root,1)]
    result=[]
    while queue:
        current,depth=queue.pop(0)
        if depth>l:
            break
        if current:
            result.append(str(current.data))
            queue.append((current.left,depth+1))
            queue.append((current.right, depth + 1))
        else:
            result.append("null")
    return result


preorder=[3,2,1,5,4]
preorder1=[3,9,20,15,7]
inorder=[1,2,3,4,5]
inorder1=[9,3,15,20,7]
root1=Node(preorder[0])
tree=root1.build_tree(preorder,inorder)
l=maximum_length(tree)
k=level_traversal(tree,l)
print(",".join("null" if _ is None else str(_) for _ in k))
print(l)


























