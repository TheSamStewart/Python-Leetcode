from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        '''
        from the root, keeping track of depth - append the rightmost value of the tree to the array

        if we append to the left, rightmost value of the queue will be the rightmost node of the tree at that depth
        
        order we need to keep in the deque - append the the right most value to the left of the deque first and keep track of this value at each loop iteration
        '''

        if not root: return []

        res = []

        queue = deque([root])

        while queue:

            current_level = len(queue)

            #this is the rightmost node, append to res

            right_side = queue[-1]

            res.append(right_side.val)

            for _ in range(current_level):
           
                current = queue.pop()

                if current.right:

                    queue.appendleft(current.right)

                if current.left:

                    queue.appendleft(current.left)

        return res
