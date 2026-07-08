"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        #Early exit cases

        if not node:

            return None 

        if not node.neighbors:

            return Node(node.val)

        #Dict to store created nodes

        nodes = {}

        def clone(node):

            #If node exists return the node from the dict

            if node.val in nodes:

                return nodes[node.val]

            #Create copy and add to dict

            copy = Node(node.val)

            nodes[node.val] = copy

            for neighbor in node.neighbors:

                #Append the recursively cloned neighbor to the current copy's neighbor list

                copy.neighbors.append(clone(neighbor))

            return copy

        return clone(node)
