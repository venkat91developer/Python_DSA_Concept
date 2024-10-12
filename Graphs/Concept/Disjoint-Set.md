# DISJOINT SET
###### A disjoint set, also known as a disjoint-set data structure or union-find, is a collection of non-overlapping (disjoint) sets. It supports two primary operations:

Find: Determines which set a particular element belongs to. This operation can help check if two elements are in the same set.
Union: Merges two sets into a single set. This is useful for combining groups of elements.
Key Features
Efficiency: Disjoint-set structures are optimized for efficiency, especially with techniques like path compression (to make the find operation faster) and union by rank (to keep trees flat during union operations).
Applications: They are widely used in algorithms like Kruskal's for minimum spanning trees, network connectivity problems, and clustering.

==Time Complexity: O(4 alpha) ~ => O(1)==

```py
class DisjoinSet:
    def __init__(self,n):
        self.rank = [0] * (n+1)
        self.size = [1] * (n+1)
        self.parent = [i for i in range(n+1)]
    
    def findParent(self,x):
        if x != self.parent[x]:
            self.parent[x] = self.findParent(self.parent[x])
        return self.parent[x]
    
    def unionByRank(self,u,v):
        pu = self.findParent(u)
        pv = self.findParent(v)
        if pu == pv:
            return 
        if self.rank[pu] > self.rank[pu]:
            self.parent[pv] = pu
        elif self.rank[pu] < self.rank[pu]:
            self.parent[pu] = pv
        else:
            self.parent[pv] = pu
            self.rank[pu]+=1

    def unionBySize(self,u,v):
        pu = self.findParent(u)
        pv = self.findParent(v)
        if pu == pv:
            return
        if self.size[pu] > self.size[pu]:
            self.parent[pv] = pu
            self.size[pu]+=self.size[pv]
        else:
            self.parent[pu] = pv
            self.rank[pv]+=self.size[pu]
```