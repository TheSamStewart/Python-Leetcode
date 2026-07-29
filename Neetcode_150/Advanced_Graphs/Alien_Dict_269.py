from collections import defaultdict, deque

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        '''
        U - Understand: Rewrite question, identify constraints, discuss assumptions and edge cases. Ask clarifying questions.

        Strings in word are sorted by alphabetical order - if not return ""

        Cases where the words array is invalid:

        if len(words[i]) > len(words[i+1]) but needs to be a prefix abc < ef is okay and means e < f
        if we prove n < f, then we find f < n this is invalid its actually a cycle so could check during traversal

        Question rewrite:

        We need to traverse words, mapping words[i] to words[i+1]. Edges mean node a < node b.
        After mapping we need to traverse the graph and return it in lexicographically increasing order.

        M - Match: Map the problem to known abstract data types (FIFO/Key-Value) or algorithmic patterns (e.g., dynamic programming, sliding window).

        This is a directed acylic (no-cycle) graph creation and traversal problem

        P - Plan: Write pseudocode. Validate logic on paper/paint sequentially before writing code.

        I - Implement: Translate the plan into clean, production-ready code.

        R - Review: Walk through the code line-by-line using dry-run inputs.

        E - Evaluate: Analyse time and space complexity and identify potential bottlenecks.

        I - Iterate: Attempt to find a better solution if possible. 
        '''

        adj = {c : set() for word in words for c in word}

        #Keep track of in-degree (how many incoming edges) for each node

        in_degree = {c : 0 for c in adj} 
        res = []

        #Iterate through words and populate the graph

        for i in range(len(words)-1):

            word1, word2 = words[i], words[i+1]

            #Returns empty string if lexico order is broken

            if len(word1) > len(word2) and word1.startswith(word2):

                return ""

            #Iterates through each word checking for char mismatch

            for j in range(min(len(word1), len(word2))):

                if word1[j] != word2[j]:
                    if word2[j] not in adj[word1[j]]:

                        #Update adjacency dict and in degree

                        adj[word1[j]].add(word2[j])
                        in_degree[word2[j]] += 1

                    break

        #Add all nodes with degree zero to the queue

        queue = deque([char for char in in_degree if in_degree[char] == 0])

        while queue:

            node = queue.popleft()

            #Append this node to res as it is next in the order

            res.append(node)

            for c in adj[node]:
                
                #Decrement in degree so we know which nodes to add to process next

                in_degree[c] -= 1

                if in_degree[c] == 0:

                    queue.append(c)

        #If there is a length mismatch this means some amount of nodes never hit degree zero, signalling a cycle

        return "".join(res) if len(res) == len(adj) else ""


