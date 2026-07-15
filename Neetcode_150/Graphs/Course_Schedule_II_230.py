class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        '''
        keep track of underway: we keep track of underway as if a course we have underway is a prereq, the solution is invalid

        keep track of completed: we keep track of completed beacuse

        dictionary of course and their prereqs, when we run into a course - until the course is completed (all prereqs are done and it doesnt appear in the next prereq) we can remove this course from underway to completed

        prereqs is adjacency matrix: in order to take A you must take course B
        as a graph this translates to in order to go to A is connected to B - How can we figure out whether we can take all courses by following these mappings and ensuring no cycle appears. 

        
        '''
        self.res = []

        #dictionary to map course to list prereqs A -> [B]

        adjacency = {i : [] for i in range(numCourses)}

        #Set for underway and completed - 
        #if task in underway and it is a pre req NOT FINE 
        #if task in completed FINE 

        underway = set()
        completed = set()

        #map our adjacency matrix

        for course, pre in prerequisites:

            adjacency[course].append(pre)
        

        #DFS to check each courseID and if it contains any cycles

        def dfs(course):

            if course in underway:
                return False
            if course in completed:
                return True

            #Set course as underway

            underway.add(course)

            #If a prereq is completed or not seen yet this will return True - if it is underway return False

            for pre in adjacency[course]:

                if not dfs(pre):

                    return False

            #Append the course taken to results array

            underway.remove(course)
            completed.add(course)
            self.res.append(course)

            return True

        #Check each courseID for Cycles

        for course in range(numCourses):

            if not dfs(course):

                return []

        return self.res
