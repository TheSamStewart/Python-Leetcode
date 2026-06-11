import math
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        res = []
        distances = []
        
        if len(points) == k:

            return points

        #calculate the distance to origin in place

        for i, point in enumerate(points):

            x , y = (point[0])**2 , (point[1])**2

            distance = math.sqrt(x+y)

            distances.append([distance, i])


        #heapify and pop of the top K times

        heapq.heapify(distances)

        for _ in range(k):

            #return k closest to origin
           
           res.append(points[heapq.heappop(distances)[1]])
        
        return res
