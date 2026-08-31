class Solution:
    def canJump(self, nums: List[int]) -> bool:
        '''
        What criteria means we cant make it to the end of the array? - 
        We dont always want to choose the max jump value. 

        '''
        
        max_reach = 0
        
        for i, num in enumerate(nums):

            #if current index outside of our max reach, we cant reach the end

            if i > max_reach:
                return False

            #calculate max reach from here - either current max reach or new max reach
            max_reach = max(max_reach, i + num)
            
        return True
