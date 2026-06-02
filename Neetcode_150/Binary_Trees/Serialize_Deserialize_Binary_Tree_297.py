# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque 

class Codec:

    def level_order(self,root):

        #algorithm that creates level order algo to serialize

        if not root: return []

        res = []

        queue = deque([root])

        while queue:

            #this stops the algorithm if all nodes in the queue(on this level) are none

            if all(node is None for node in queue):
                break

            current_level_len = len(queue)

            for _ in range(current_level_len):

                current = queue.popleft()

                to_append = None if current is None else current.val

                res.append(to_append)

                if current is None:

                    continue

                queue.append(current.left)

                queue.append(current.right)

        return res

    def serialize(self, root):

        """
        input = list of tree nodes in level order 
        output = string of binary representations of tree nodes in level order 
        encode = [1-bit null indicator][11-bit 2's compliment]
                    

        ALGO

        1 - start loop to iterate through each node in the tree
        2 - for each node in the tree convert to binary equivalent
        EDGE CASE: if node is null, we represent as null in the string - has to be sequence of bits, how can we represent null? - we add an extra bit to indicate null
        EDGE CASE: value of node can be negative - encode using 11 bit 2s compliment (represents -1024 -> 1023) 
        """

        encoded = ""

        level_order_list = self.level_order(root)

        #if there is not root we return the empty string 

        if level_order_list == []: return encoded
        
        for node in level_order_list:

            encoded_node = ""

            #if the node is None we set our null bit to 1 else 0 

            if node is None:
                encoded_node += "100000000000"
            else:
                encoded_node += "0"
           
                

            #if node is null we append the encoded node to the string and continue to the next node

            if node is None:

                encoded += encoded_node

                continue            

           
            #if node is pos or 0, we convert to binary and append to the encoded string

            if node >= 0:

                binary_value = (bin(node))[2:]
                
                #calculate leading zeros

                zeros_to_add = 11 - len(binary_value)

                #add the zeros to the encoded node and add to encoded string 

                for _ in range(zeros_to_add):

                    encoded_node += "0"

                encoded_node += str(binary_value) 

                encoded += encoded_node

            #else the number is negative

            else:

                #first we need the positive value to convert into twos compliment

                positive_value = abs(node)

                #flip the bits and AND with our mask to ignore the bits we do not need

                twos_comp = ~positive_value & ((1 << 11)-1)

                #add one

                twos_comp += 1

                #format to binary

                twos_comp = format(twos_comp, '011b')

                encoded_node += str(twos_comp)

                encoded += encoded_node 

        return encoded
        

    def deserialize(self, data):
        """
        ALGO 

        1. for each 12 bit bin number in data 
        2. check if b12 is 1 - if yes null
        3. check if b11 is 1 - if yes convert from twos comp to decimal else convert from bin to decimal
        4. create a list of nodes at each node append the value to the list
        5. using the level order traversal create the tree
        """

        #define the root for return

        root = None

        level_order_list = []

        #use for loop to keep track of offset

        for offset in range(0, len(data), 12):

            #get each 12 bit node

            node = data[offset : offset + 12]

            #check for null

            if node[0] == "1":

                level_order_list.append('null')

            #check for twos comp

            elif node[1] == "1":
              
                raw_val = int(node[1:], 2)
                
                decimal_value = raw_val - 2048

                level_order_list.append(decimal_value)

            #else node value is pos number

            else:

                raw_value = int(node[1:], 2)

                level_order_list.append(raw_value)

        if not level_order_list or level_order_list[0] is None:
            return None

        root = TreeNode(level_order_list[0])

        queue = deque([root])

        list_index = 1

        #loop to create the tree

        while queue and list_index < len(level_order_list):

            #pop the leftmost node off

            current = queue.popleft()

            if list_index < len(level_order_list):

                #create the node

                left_val = TreeNode(level_order_list[list_index])
                list_index += 1

                #if the node has a value append as the left child

                if left_val is not None:

                    current.left = left_val
                    queue.append(current.left)

            #do same but for right

            if list_index < len(level_order_list):

                right_val = TreeNode(level_order_list[list_index])
                list_index += 1

                if right_val is not None:

                    current.right = right_val
                    queue.append(current.right)

        return root
