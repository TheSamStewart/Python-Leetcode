from collections import Counter

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        '''
        ababcbaca defegde hijhklij

        Criteria for creating a partiton - there is no occurence of any of the chars in the position past this point

        We iterate through the string decrementing counts, when we have found the last instance of a charachter, when we next find a new charachter - this is the end of the partition
        '''

        res = []
        #Count frequency so we know when we have hit the last occurence
        freq = Counter(s)
        n = len(s)
        #Set to store the values in which have occurences left
        current = set()
        start = 0

        for i in range(n):

            #add the char to current and decrement frequency

            current.add(s[i])
            freq[s[i]] -= 1

            if freq[s[i]] == 0:

                #we are done with this character

                current.discard(s[i])

            #if current is empty this partition is finished append the length
            if not current:

                res.append(i - start + 1)
                start = i + 1

        return res

            





            



        


        
