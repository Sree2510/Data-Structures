import heapq
from heapq import heappop, heappush

n=4
arr=[4,3,2,6]
# arr.sort()
# ans=[]
# while len(arr)!=1:
#     n1=arr.pop(0)
#     n2=arr.pop(0)
#     sum1=n1+n2
#     ans.append(sum1)
#     arr.insert(0,sum1)
#     arr.sort()
# print(sum(ans))

heapq.heapify(arr)
t=0
while len(arr)>1:
    n1=heappop(arr)
    n2=heappop(arr)
    sum=n1+n2
    t+=sum
    heappush(arr,sum)
print(t)