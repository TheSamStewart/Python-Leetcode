class TrieNode:

    def __init__(self):

        self.children = {}
        self.is_end = False

class WordDictionary:

    def __init__(self):

        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:

        curr = self.root

        for c in word:

            if c not in curr.children:

                curr.children[c] = TrieNode()

            curr = curr.children[c]

        curr.is_end = True
        
    def search(self, word: str) -> bool:

        def checkWord(node, index):

            if index == len(word):

                return node.is_end 

            if word[index] != '.':

                if word[index] not in node.children: return False

                nextNode = node.children[word[index]]

                correct = checkWord(nextNode, index+1)

                if correct: return True

            else:

                for child in node.children.values():

                    correct = checkWord(child, index+1)

                    if correct: return True

            return False

        return checkWord(self.root,0)
