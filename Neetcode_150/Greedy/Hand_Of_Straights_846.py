from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        #We can sort the array
        
        #Count the frequency of each card

        #Take each lowest frequency as f, if f+1,f+2 exist, decerement their counts and continue
        
        #if it doesnt exist return false

        if len(hand) % groupSize != 0:
            return False

        counts = Counter(hand)

        for card in sorted(counts):
            #Check if we have used this card for previous groups

            if counts[card] > 0:

                #Count of how many groups we need to make from here

                start_count = counts[card]

                #Iterate through the consecutive cards

                for i in range(card, card+groupSize):

                    #If the count is less than the amount of groups we need return False

                    if counts[i] < start_count:

                        return False
                        
                    start_count -= 1

        return True





        
        
