class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        '''
        All nodes in the left subtree of a node contain values strictly less than the node’s value.
        All nodes in the right subtree of a node contain values strictly greater than the node’s value.

        Ancestor = you have to pass this node to get to the stated node
        '''

        def findAncestor(node):

            if not node: return 

            #check if this is the LCA

            if (node.val > p.val and node.val < q.val) or (node.val < p.val and node.val > q.val) or (node.val == q.val or node.val == p.val):

                return node
            
            #first check if the current node is smaller than both values, if so take the left path

            if node.val < p.val and node.val < q.val:
            
               return findAncestor(node.right)

            #second check if the current node is larger than both values, take the right path

            if node.val > p.val and node.val > q.val:

               return findAncestor(node.left)

        return (findAncestor(root))
