n,m=map(int,input().split())
"""
undirected graph adjacency matrix method

adjacent_matrix=[[0 for i in range(n+1)]for i in range(n+1)]
for i in range(m):
    a,b=map(int,input().split())
    adjacent_matrix[a][b]=1
    adjacent_matrix[b][a]=1
for i in adjacent_matrix:
    print(i)
"""
#undirected graph adjacency list method
adjacent_list=[[] for i in range(n+1)]
for i in range(m):
    a,b=map(int,input().split())
    adjacent_list[a].append(b)
    adjacent_list[b].append(a)
print(adjacent_list)
"""
#directed graph adjacency list method
adjacent_list=[[] for i in range(n+1)]
for i in range(m):
    a,b=map(int,input().split())
    adjacent_list[a].append(b)
print(adjacent_list)"""