import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        '''
        First create adjacency list to detect cycles
        Use a minheap to store edge:weight pairs

        Pop off the minheap, and detect cycle. If the edge creates a cycle discard, when we have visited all nodes, we can return the min time
        '''

        adj = {i+1 : [] for i in range(0,n)}
        min_heap = []
        visited = set()

        for source,target,time in times:

            adj[source].append((time,target))

        heapq.heappush(min_heap, (0,k))
        
        while min_heap:

            current_weight, current_node = heapq.heappop(min_heap)

            if current_node not in visited:

                visited.add(current_node)

                if len(visited) == n:

                    return current_weight

                for new_weight, new_node in adj[current_node]:

                    if new_node not in visited:

                        heapq.heappush(min_heap ,(new_weight + current_weight, new_node))

        

        return -1

            



        
