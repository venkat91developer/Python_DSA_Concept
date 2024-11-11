from typing import List
from collections import defaultdict
class Solution:
    def dfs(self,start,target,graph,visited=None):
        if visited is None:
            visited = set()
        visited.add(start)
        if start == target:
            return True
        for child in graph[start]:
            if child not in visited:
                if self.dfs(child,target,graph,visited):
                    return True
        return False

    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int):
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        return self.dfs(source,destination,graph)
obj = Solution()
edges = [[0,1],[1,2],[2,0]]
n = 3
print(obj.validPath(n,edges,0,2))