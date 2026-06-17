import heapq
class MedianFinder:

    def __init__(self):

        self.count = 0
        self.min_heap = []
        self.max_heap = []
        

    def addNum(self, num: int) -> None:

        #if this is the first number add max heap by default
        if self.count == 0:
                
            heapq.heappush(self.max_heap, -num)

            self.count += 1

            return 

        #if this isnt the first number compare with the top value of the max heap
        if num < -(self.max_heap[0]):
            
            heapq.heappush(self.max_heap, -num)

        else:

            heapq.heappush(self.min_heap, num)

        #check if heaps are balanced
        
        #if min heap is smaller than max heap and the difference between the lengths is greater than one 
        if len(self.max_heap) - len(self.min_heap) > 1:

            #pop from the max heap and push to the min heap
            val = heapq.heappop(self.max_heap)

            heapq.heappush(self.min_heap, -val)

        #same but for the max heap
        elif len(self.min_heap) - len(self.max_heap) > 1:

            val = heapq.heappop(self.min_heap)

            heapq.heappush(self.max_heap, -val)

        self.count += 1

    def findMedian(self) -> float:

        if self.count % 2 == 0:

            return (-(self.max_heap[0]) + self.min_heap[0]) / 2

        else:

            if len(self.min_heap) > len(self.max_heap):

                return self.min_heap[0]
            
            else:

                return -self.max_heap[0]
