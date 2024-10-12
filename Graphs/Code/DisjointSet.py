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


obj = DisjoinSet(7)
obj.unionByRank(1,2)
obj.unionByRank(2,3)
obj.unionByRank(4,5)
obj.unionByRank(6,7)
obj.unionByRank(5,6)
#Find 3 belongs to 7 Same Component
print('RANK: ',obj.rank)
print('PARENT: ',obj.parent)
if obj.findParent(3) == obj.findParent(7):
    print('Same')
else:
    print('Not Same')

obj.unionByRank(3,7)
print('RANK: ',obj.rank)
print('PARENT: ',obj.parent)
if obj.findParent(3) == obj.findParent(7):
    print('Same')
else:
    print('Not Same')

