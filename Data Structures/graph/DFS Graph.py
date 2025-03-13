def solve_dfs(ad,v,k):
    v[k]==1
    print(k)
    for i in ad[k]:
        if v[i]==0:
            solve_dfs(ad,v,i)


n,m=map(int,input().split())
adjacent_list=[[] for i in range(n+1)]
visited=[0 for i in range(n+1)]
for i in range(m):
    a,b=map(int,input().split())
    adjacent_list[a].append(b)
solve_dfs(adjacent_list,visited,1)