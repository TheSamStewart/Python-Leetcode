from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        '''
        at each level, pass each nodes value into the array

        solve using deque

        '''

        if not root: return []

        res = []

        queue = deque([root])

        while queue:

            #create our current level array to append to result

            current_level = []

            #get the length of the current level

            current_level_len = len(queue)

            #for i in range len of the current level

            for _ in range(current_level_len):

            #pop off the queue, append the children and append current to the results array

            #pop left to follow FIFO

                current = queue.popleft()

                current_level.append(current.val)

                if current.left:

                    queue.append(current.left)

                if current.right:

                    queue.append(current.right)

            #return the results array

            res.append(current_level)

        return res
