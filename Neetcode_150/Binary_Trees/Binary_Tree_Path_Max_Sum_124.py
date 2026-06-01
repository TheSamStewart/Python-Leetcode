# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        '''
        
        '''

        self.res = float("-inf")

        def dfs(node):

            #When we hit none return 0 to start the count 

            if not node: return 0

            #compare the left and right paths to zero, if less than zero treat as zero as negatives are useless

            left_max = max(0, dfs(node.left))
            right_max = max(0, dfs(node.right))

            #if current path > current max path update the res variable

            self.res = max(self.res, left_max + right_max + node.val)

            #return the best(max) path to the parent node

            return max(left_max, right_max) + node.val


        dfs(root)

        return self.res
