
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        '''
        traverse the tree and add all elements to a min heap (to store as min heap we negate the value)

        min heap to store the value of the node alongside the pointer to the node in the tree? - do we even need to store the pointer 

        recursive strategy - recurse until the leftmost node is hit, once this node is hit we recurse up the tree until we hit the k smallest node 
        '''

        self.count = 0
        self.result = None

        def kthSmallest(node):

            if not node or self.result is not None:
                return

            #recurse to the leftmost node

            kthSmallest(node.left)

            #increment and perform checks

            if self.result is None:
                self.count += 1
                if self.count == k:
                    self.result = node.val
                    return

            #now to the rightnode of the leftmost

            kthSmallest(node.right)

        kthSmallest(root)

        return self.result
