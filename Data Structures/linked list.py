class Node:
   def __init__(self, data=None):
      self.data = data
      self.next = None

class LinkedList:
   def __init__(self):
      self.head = None

   def listprint(self):
      value = self.head
      while value is not None:
         print (value.data)
         value = value.next
   def find_middle(self):
       one=self.head
       two=self.head
       while two and two.next:
           one=one.next
           two=two.next.next
       if one:
           print(one.data)
   def delete_node(self,ele):
       value=self.head
       if value is not None:
           if value.data ==ele:
               self.head= value.next
               value=None
               return 1
       while value is not None:
           if value.data ==ele:
               break
           prev=value
           value=value.next
       if value==None:
           return 0
       prev.next=value.next
       value=None
       return 1


# a=int(input())
# b=list(map(int,input().split()))
b=[10,20,30,40,50]
c=int(input())
list = LinkedList()
# for i in c:
#     b.append(i)
for i in range(len(b)):
    value=Node(b[i])
    if i==0:
        list.head=value
        current=value
    else:
        current.next=value
        current=value
#list.listprint()
#list.find_middle()
k=list.delete_node(c)
if k==1:
    list.listprint()
else:
    print("Not in list")