import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        min_heap = nums[:k]
        heapq.heapify(min_heap)

        for num in nums[k:]:

            #if num is larger than the smallest element, in belongs in the top k pool
            #so we pop and push

            if num > min_heap[0]:

                heapq.heappushpop(min_heap, num)

        return min_heap[0]  
