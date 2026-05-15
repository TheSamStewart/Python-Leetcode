class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        #map each value in inorder to its index for 0(1) lookup
        
        inorder_map = {val : i for i, val in enumerate(inorder)}

        #init a pre index counter to avoid slicing

        pre_idx = 0 

        #init our helper function which takes in_left and in_right - these are our boundaries

        def helper(in_left, in_right):

            nonlocal pre_idx
            #define our base case which is no more elements - if in_left pointer > in_right pointer - they have crossed and there are no more elements
            
            if in_left > in_right: return None

            #select the current root from preorder and increment the pointer

            root_val = preorder[pre_idx]
            root = TreeNode(root_val)
            pre_idx += 1

            #find the split point in inorder using the map

            pivot = inorder_map[root_val]

            #build the subtrees - root.left = (in_left, pivot-1) - root.right = (pivot+1,in_right)
            
            root.left = helper(in_left, pivot-1)
            root.right = helper(pivot+1, in_right)

            return root

        #return the root to the parent for processing

        return helper(0, len(inorder) - 1)
