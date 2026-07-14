class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        '''

        [[1,0]] to take course 1 pre req is course 0

        [[1,0] [0,1]] to take course 1, you need to take 0. to take course 0 you need 1.

        have to take bi to take course ai.

        If there is a cycle in numbers 1 -> 0 -> 0 -> 1 - this cant be true as you can never take course 1 or 0. 

        to be true it would need to be 1 -> 0 -> 0 -> 2

        WHAT WE NEED TO PROVE: that we can move through the prereq array without finding a cycle. 

        numCourses = valid courseIDs

        '''

        adjacency = {i : [] for i in range(numCourses)}

        for course,pre in prerequisites:

            adjacency[course].append(pre)

        underway = set()
        completed = set()

        def dfs(course):

            if course in underway:
                return False
            if course in completed:
                return True

            underway.add(course)

            #check each pre, if underway - cycle detected return False

            for pre in adjacency[course]:
                if not dfs(pre):
                    return False

            underway.remove(course)
            completed.add(course)

            return True


        for course in range(numCourses):

            if not dfs(course):

                return False

        return True


        



        
