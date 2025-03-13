# from collections import deque
#
# arr=list(map(int,input().split()))
# arr.sort()
# t=int(input())
# queue=deque()
# for i in range(len(arr)):
#     queue.append(arr[i])
# res=[]
# c=0
# while queue:
#     k=queue.popleft()
#     if k==t:
#         res.append(c)
#     if k>t:
#         break
#     c+=1
# ans=[]
# ans.append(res[0])
# ans.append(res[-1])
# print(ans)
#
#

# arr=list(map(int,input().split()))
# target=int(input())
# res=[]
# if not arr:
#     print([-1,-1])
# for i in range(len(arr)):
#     if target==arr[i]:
#         res.append(i)
#     elif target<arr[i]:
#         break
# if res:
#     print([res[0],res[-1]])
# else:
#     print(-1,-1)
#



# from collections import Counter as c
# a=[5,5,10,12,12,12]
# s=c(a)
# print(s[12])

#
# a="Leetcode"
# a1=a[::-1]
# print(a[0],a1[0])

# s="IceCreAm"
# V=['A','E','I','O','U','a','e','i','o','u']
# arr=""
# for i in s:
#     if i in V:
#         arr+=i
# arr1=arr[::-1]
# ans=""
# c=0
# for i in s:
#     if i in V:
#         ans+=arr1[c]
#         c+=1
#     else:
#         ans+=i
# print(ans)

# a=("The Sky is Blue")
# a=a.split()
# ans=[]
# for i in a[::-1]:
#     ans.append(i)
# print(ans)

a=[1,2,3,4]
l=1
r=1
res=[1]*len(a)
print(a)
for i in range(len(a)):
    res[i]=r
    r*=a[i]
print(res)
for i in range(len(a)-1,-1,-1):
    res[i]*=l
    l*=a[i]
print(res)
