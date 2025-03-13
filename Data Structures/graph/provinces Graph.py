def solve_dfs(ad,v,k):
    v[k]=1
    for i in ad[k]:
        if v[i]==0:
            solve_dfs(ad,v,i)

n,m=map(int,input().split())
adjacent_matrix=[[0 for i in range(n+1)] for i in range(n+1)]
for i in range(m):
    a,b=map(int,input().split())
    adjacent_matrix[a][b]=1
    adjacent_matrix[b][a]=1
adjacent_list=[[] for i in range(n+1)]
for i in range(len(adjacent_matrix)):
    for j in range(len(adjacent_matrix[0])):
        if adjacent_matrix[i][j]==1 and i!=j:
            adjacent_list[i].append(j)
            adjacent_list[j].append(i)
visited=[0 for i in range(n+1)]
c=0
for i in range(1,n+1):
    if visited[i]==0:
        c+=1
        solve_dfs(adjacent_list,visited,i)
print(c)