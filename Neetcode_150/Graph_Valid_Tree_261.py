class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        #Init Adjacency dict
        adj = {i : [] for i in range(n)}

        for node1,node2 in edges:

            adj[node1].append(node2)
            adj[node2].append(node1)

        #Set to track visited nodes for cycle

        visited = set()

        def dfs(node, parent):

            #If current node has already been visited this is a cycle

            if node in visited:

                return False

            visited.add(node)

            #Now we call the function on each neighbouring node

            for neighbour in adj[node]:

                if neighbour == parent:

                    continue

                if not dfs(neighbour,node):

                    return False

            return True

        #Start the DFS from the 0th node

        if not dfs(0,-1):

            return False

        #This ensures that all nodes are connected as dfs function doesnot check for this

        return len(visited) == n

                





         
        
