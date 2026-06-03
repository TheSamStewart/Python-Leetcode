class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:

    def __init__(self):

        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        
        #start at the root 

        curr = self.root

        #loop through the word

        for c in word:

            #if char doesnt exist add it to current.children and link the trie node

            if c not in curr.children:
                
                curr.children[c] = TrieNode()

            #move pointer to new node
            
            curr = curr.children[c]

        #mark end of word

        curr.is_end = True
        

    def search(self, word: str) -> bool:

        #start at the root
        curr = self.root

        #loop through the word
        for c in word:

        #if the char doesnt exist in current.children return False
            if c not in curr.children:
                
                return False

            #move pointer to next node

            curr = curr.children[c]
        
        return curr.is_end
       
    def startsWith(self, prefix: str) -> bool:

        curr = self.root

        for c in prefix:

            if c not in curr.children:

                return False

            curr = curr.children[c]

        return True