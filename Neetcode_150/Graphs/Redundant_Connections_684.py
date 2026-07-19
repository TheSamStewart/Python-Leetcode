class UnionFind:

    def __init__(self, size):

        self.parent = list(range(size))

    def find(self, node):

        #If the nodes parent is the node, this is the root
        if self.parent[node] == node:
            return node
          
        #This sets the current nodes parent as the absolute root, dont need to traverse each node inbetween parent and node to find parent 
        self.parent[node] = self.find(self.parent[node])

        return self.parent[node]

    def union(self, a, b):

        root_a = self.find(a)
        root_b = self.find(b)

        #If root is not already the parent, set it as the parent

        if root_a != root_b:

            self.parent[root_a] = root_b

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        '''
        Create adj dict 
        Check for all cycles
        Last Cycle detected is the returned coord

        nodes are labelled form 1 -> n 

        How to check for cycle:

        Set to check if node has been visited

        iterate through nodes from 1 -> n as graph is guaranteed to be connected or using DFS approach start the DFS from 1

        '''

        uf = UnionFind(len(edges)+ 1)

        #if a path exists between a and b, then this creates a cycke so return

        for a,b in edges:

            if uf.find(a) == uf.find(b):

                return [a,b]

            uf.union(a,b)

            



        
