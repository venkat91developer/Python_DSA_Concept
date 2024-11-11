from collections import defaultdict, deque
from typing import List

class Solution:
    def getAdj(self, a: List[List[int]]) -> dict:
        n = len(a)
        graph = defaultdict(list)
        for i in range(n):
            for j in range(n):
                if i != j and a[i][j]:
                    graph[i].append(j)
        return graph
    
    def bfs(self, start, graph, visit):
        queue = deque([start])
        visit[start] = True
        while queue:
            current = queue.popleft()
            for child in graph[current]:
                if not visit[child]:
                    visit[child] = True
                    queue.append(child)

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph = self.getAdj(isConnected)
        n = len(isConnected)
        visit = [False] * n
        counter = 0
        for i in range(n):
            if not visit[i]:
                counter += 1
                self.bfs(i, graph, visit)
        return counter
