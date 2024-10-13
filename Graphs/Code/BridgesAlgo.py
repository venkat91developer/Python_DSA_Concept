class Solution:
    def __init__(self):
        self.timer = 1
    def dfs(self,node,parent,visit,graph,time,low,bridges):
        visit[node]= True
        low[node] = time[node] = self.timer
        self.timer+=1
        for child in graph[node]:
            if child == parent:
                continue
            if not visit[child]:
                self.dfs(child,node,visit,graph,time,low,bridges)
                low[node] = min(low[node],low[child])
                if low[child]>time[node]:
                    bridges.append([node,child])
            else:
                low[node] = min(low[node],low[child])
    def criticalConnections(self, n: int, connections: List[List[int]]):
        graph = collections.defaultdict(list)
        for u,v in connections:
            graph[u].append(v)
            graph[v].append(u)
        visit = [False] * n
        time,low,bridges = [0]*n,[0]*n,[]
        self.dfs(0,-1,visit,graph,time,low,bridges)
        return bridges
'''
TIME COMPLEXITY: 
i) O(N+E)
   for u,v in connections:
        graph[u].append(v)
        graph[v].append(u)
ii)DFS O(N+2E)
=> O(N+E)

SPACE COMPLEXITY:
O(4N+E)
'''