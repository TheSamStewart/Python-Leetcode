from collections import deque

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        '''
        Assume we have zero edges so components = n

        As we add edges we decrement the amount of components
        If adding component creates a cycle, we do not decrement components - we need cycle detection
        '''

        visited = set()
        components = 0

        #Create adjacency dict

        adj = {i : [] for i in range(n)}

        for node1,node2 in edges:

            adj[node1].append(node2)
            adj[node2].append(node1)

        #Loop through each node as we are guaranteed 0 -> n-1 nodes

        for i in range(n):

            #If this is an unvisited node, perform a BFS from here

            if i not in visited:

                dq = deque([i])

                components += 1

                while dq:

                    current = dq.popleft()

                    if current in visited:

                        continue 

                    visited.add(current)

                    #For each neighbour of this node append them to the queue for processing

                    for neighbour in adj[current]:

                        if neighbour not in visited:

                            dq.append(neighbour)

        return components

        
