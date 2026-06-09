import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        #negate all stone values for max heap
        
        stones = [-x for x in stones]

        #init the max heap

        heapq.heapify(stones)

        #while we have stones to break

        while len(stones) > 1:

            #pop the two largest values

            x = heapq.heappop(stones)
            y = heapq.heappop(stones)

            #undo negation

            x , y = -x, -y

            #if the stones arent equal

            if x != y:

                #get new stone value and add to heap

                new_stone = x - y

                heapq.heappush(stones, -new_stone)

            #return the value of the last stone if last stone else 0

        return -stones[0] if stones else 0
