class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        '''
        subtree can be subtree of itself 

        condition for subroot "tree that consists of a node in tree and all its descendants are equal"1

        first we can iterate through the tree to find a node that matches(root.val and root.left.val and root.right.val) the subroot

        if it matches we then recursively check all nodes in both trees to see if they are the same
        '''

        #start recursive function that check each node in the root tree

        
         #this checks the subtree
        def checkSubtree(node1, node2):

            #if both are null this is a match
            if not node1 and not node2:
                return True

            #if mismtach return false
            if (bool(node1) ^ bool(node2)): 
                return False

            #if mismtach return false
            if node1.val != node2.val: 
                return False

            #check left nodes
            check_left = checkSubtree(node1.left, node2.left)
            if check_left == False:
                return False

            #check right nodes
            check_right = checkSubtree(node1.right, node2.right)
            if check_right == False:
                return False

            #if we have made it to here its a match
            return True  

        
        def findStartNode(node):

            #if we are at the end of the tree we just return to the parent node

            if not node:
                return False

            #if the nodes are the same 

            if node.val == subRoot.val:

              #if the subtrees are the same return True

                if (checkSubtree(node, subRoot)):

                    return True
                  
            #call the function on all nodes until return True

            return ((findStartNode(node.left)) or (findStartNode(node.right)))

            
        
        return findStartNode(root)
