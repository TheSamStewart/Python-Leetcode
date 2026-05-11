class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        '''
        good node means node is larger than the current max in its path 

        using recursion, pass in current max each time?
        '''
        
        def findGoodNodes(node, current_max):

            if not node: return 0

            count = 1 if node.val >= current_max else 0 
            
            current_max = max(current_max, node.val)

            count += findGoodNodes(node.left,current_max)

            count += findGoodNodes(node.right,current_max)

            return count

        return findGoodNodes(root, float('-inf'))
