# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        '''
        left subtree must contain nodes with keys strictly less than
        right subtree must contain nodes with keys strictly greater than

        all child nodes of the current nodes must follow the BST criteria
        '''

        def checkBST(node, low, high):

            if not node: return True

            #check the inherited boundaries at each stage

            if not (low < node.val < high):
                return False

            #call the function on the left and right side of the tree
            #if false is returned once it is returned up the tree because of the and

            return (
                    (checkBST(node.left, low, node.val)) and 
                    (checkBST(node.right, node.val, high))
                    )

        
        return checkBST(root, float('-inf'), float('inf'))
