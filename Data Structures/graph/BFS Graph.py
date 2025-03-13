
def bfs(adjacent_list,visited):
    queue=[1]
    while queue:
        k=queue.pop(0)
        if visited[k]==0:
            visited[k]=1
            for i in adjacent_list[k]:
                queue.append(i)
            print(k,end=" ")

n,m=map(int,input().split())
adjacent_list=[[] for i in range(n+1)]
visited=[0 for i in range(n+1)]
for i in range(m):
    a,b=map(int,input().split())
    adjacent_list[a].append(b)
    adjacent_list[b].append(a)
bfs(adjacent_list,visited)
print()
print(adjacent_list)
print(visited)