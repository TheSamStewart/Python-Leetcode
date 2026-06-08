class TrieNode:

    def __init__(self):

        self.children = {}

        self.is_end = False

        self.index = None



class Trie:

    def __init__(self):

        self.root = TrieNode()



    def search(self, word):

        current = self.root

        for letter in word:

            if letter not in current.children:

                return False

            current = current.children[letter]

        return current.is_end



    def insert(self, word, index):

        current = self.root

        for letter in word:

            if letter not in current.children:

                current.children[letter] = TrieNode()

            current = current.children[letter]

        current.is_end = True

        current.index = index

    def remove(self, word):

        if not self.search(word):

            return

        def remove_helper(current_node, index):

            #Base Case we are the end of the word, we can unselect this as the end of a word

            if len(word) == index:

                current_node.is_end = False

                current_node.index = None

                #tell the parent function whether this node can be deleted or not

                return len(current_node.children) == 0

            letter = word[index]

            next_node = current_node.children[letter]

            #recursively call on each node for each letter

            should_delete_child = remove_helper(next_node, index + 1)

            if should_delete_child:

                current_node.children.pop(letter)

                #if this evaluates to true this means the current node is not important to any other word and is not the end if another word

                return len(current_node.children) == 0 and not current_node.is_end

            return False

        current = self.root

        #removes the first node if allowed

        if remove_helper(current, 0):

            current.children.pop(word[0]) 



class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        def dfs(r, c, node):

            #check for bounds or used letter or letter not in Trie

            if (r < 0 or r >= ROWS or
            c < 0 or c >= COLS
            or board[r][c] == '#'
            or board[r][c] not in node.children):

                return

            #check if the current node is the end of the word, if so add the word to result array

            char = board[r][c]
            next_node = node.children[char]

            if next_node.is_end:

                self.res.append(words[next_node.index])

                next_node.is_end = False


            #mark the used square 

            board[r][c] = '#'
 
            #call the recursive function

            dfs(r+1,c,next_node)
            dfs(r-1,c,next_node)
            dfs(r,c+1,next_node)
            dfs(r,c-1,next_node)

            #restore the board 

            board[r][c] = char
            
        self.Trie = Trie()

        #fill the Trie

        for i, word in enumerate(words):

            self.Trie.insert(word, i)

        self.res = []

        #init boundaries

        ROWS = len(board)
        COLS = len(board[0])

        #iterate through each letter ont the board

        for r in range(ROWS):

            for c in range(COLS):

                dfs(r, c, self.Trie.root)

        return self.res
