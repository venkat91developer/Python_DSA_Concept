from typing import List
from collections import deque
import heapq
class Solution:
    def dijkstra(self, V: int, adj: List[List[int]], S: int) -> List[int]:
        heap = [(0,S)]
        dist = [float('inf') for _ in range(V)]
        dist[S] = 0
        while heap:
                NodeWeight,Node = heapq.heappop(heap)
                for ChildNode,ChildWeight in adj[Node]:
                    if NodeWeight+ChildWeight < dist[ChildNode]:
                        dist[ChildNode] =  NodeWeight+ChildWeight
                        heapq.heappush(heap,(NodeWeight+ChildWeight,ChildNode))
        return dist
    def shortest_path_length(self, V: int, adj: List[List[int]], src: int, des: int) -> int:
        dist = self.dijkstra(V, adj, src)
        return dist[des] if dist[des] != float('inf') else -1
    def dijkstra_with_path(self, V: int, adj: List[List[int]], src: int, des: int) -> List[int]:
        heap = [(0, src)]
        dist = [float('inf')] * V
        dist[src] = 0
        parent = [-1] * V
        while heap:
            NodeWeight, Node = heapq.heappop(heap)
            
            for ChildNode, ChildWeight in adj[Node]:
                if NodeWeight + ChildWeight < dist[ChildNode]:
                    dist[ChildNode] = NodeWeight + ChildWeight
                    parent[ChildNode] = Node
                    heapq.heappush(heap, (NodeWeight + ChildWeight, ChildNode))
        if dist[des] == float('inf'):
            return []  # Destination not reachable
        path = []
        current = des
        while current != -1:
            path.append(current)
            current = parent[current]
        return path[::-1]  # Reverse the path to get it from src to des

