import heapq
'''
#1. heapify(data)
#2. heappush(data,4)
#3. heappop(data)
#4. heappushpop(data,4)
#5. nlargest(data,3)
#6. nsmallest(data,3)
#7. heapreplace(data,3)
#8. merge
'''
data = [6,2,5,8,1,3]
heapq.heapify(data)
print(data)
heapq.heappush(data,0)
print(data)
result = heapq.heappop(data)
print(result,data)
result = heapq.heappushpop(data,4)
print(result,data)
result = heapq.heapreplace(data,1)
print(result,data)
result = heapq.nlargest(3,data)
print(result)
result = heapq.nsmallest(3,data)
print(result)   