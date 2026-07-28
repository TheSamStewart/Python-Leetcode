import heapq

class DSU:

    def __init__(self, n):
        
        self.parent = list(range(n))
    
    def find(self,i):

        #if value at i is i this is the absolute root node 

        if self.parent[i] == i:

            return i

        #recursively call find until we are at the absolute root node

        self.parent[i] = self.find(self.parent[i])

        #return current parent to set current nodes parent (compression)

        return self.parent[i]

    def union(self,u,v):

        root_u = self.find(u)
        root_v = self.find(v)

        #if roots are equal this is a cycle, return False

        if root_u == root_v:

            return False

        self.parent[root_u] = root_v

        return True 

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        #Use DSU to store nodes and their connections, if two nodes share the same parent and we add an edge - this creates a cycle 

        #Use min heap to store edges and weights

        #When we add an edge we increment edge counter - when edge counter = n-1 we return the answer

        min_cost = 0 
        min_heap = []
        edges = 0
        n = len(points)
        dsu = DSU(n)

        #populate the min heap

        for a in range(n):

            for b in range(a+1, n):

                manhattan = abs(points[a][0] - points[b][0]) + abs(points[a][1] - points[b][1])

                heapq.heappush(min_heap, (manhattan, a,b))

        #while we have edges and we havent connected all nodes

        while min_heap and edges < n-1:

            cost, u, v = heapq.heappop(min_heap)

            #use DSU to see if nodes are connected - returns True if yes

            if dsu.union(u,v):

                #update min_cost and edge counts

                min_cost += cost
                edges += 1

        return min_cost

            
