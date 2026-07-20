from collections import defaultdict
from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        '''
        BFS Approach

        1. Starting from beginWord, iterate through all valid 1 letter transformations of this word and append them to the queue (if they havent been visited)
        2. Continue the cycle until we reach endWord 
        3. Return the number of transformations 
        '''

        #check if word is present
        if endWord not in wordList:
            return 0

        #needs to be present to map adjacency 

        if beginWord not in wordList:

            wordList.append(beginWord)

        # Map words to pattern to avoid O(N^2) pairwise comparisons

        pattern_map = defaultdict(list)

        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                pattern_map[pattern].append(word)

        #dq for BFS

        dq = deque([beginWord])

        visited = {beginWord}

        count = 1

        while dq:

            #Check each valid word

            for _ in range(len(dq)):

                word = dq.popleft()
                
                #Check if this is a valid path

                if word == endWord:

                    return count

                #Iterate through patterns to find valid 1-letter transformations

                for i in range(len(word)):

                    pattern = word[:i] + "*" + word[i+1:]

                    for neighbour in pattern_map[pattern]:

                        if neighbour not in visited:
                            dq.append(neighbour)
                            visited.add(neighbour)

            count += 1

        return 0
                        

                    

                

            



        


        
