class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def build_tree(self,preorder,inorder):
        if not preorder and not inorder:
            return None
        root_value=preorder[0]
        root_index=inorder.index(root_value)
        in_left=inorder[:root_index]
        in_right=inorder[root_index+1:]
        pre_left=preorder[1:1+len(in_left)]
        pre_right=preorder[1+len(in_left):]
        root=Node(root_value)
        root.left=self.build_tree(pre_left,in_left)
        root.right=self.build_tree(pre_right,in_right)
        return root
def maximum(root):
    if not root:
        return 0
    else:
        l=maximum(root.left)
        r=maximum(root.right)
    return max(l,r)+1

def level_traversal(root,h):
    if not root:
        return ["null"]
    queue=[(root,1)]
    result=[]
    while queue:
        current,depth=queue.pop(0)
        if depth>h:
            break
        if current:
            result.append(str(current.data))
            queue.append((current.left,depth+1))
            queue.append((current.right,depth+1))
        else:
            result.append("null")
    return result 

a=list(map(int,input().split()))
b=list(map(int,input().split()))
root1=Node(a[0])
tree=root1.build_tree(a,b)
k=maximum(tree)
p=level_traversal(tree,k)
print(",".join(p))