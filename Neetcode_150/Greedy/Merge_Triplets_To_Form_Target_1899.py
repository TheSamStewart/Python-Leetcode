class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        '''
        What numbers need to exist in triplets for us to ensure that we can make a triplet

        1. All values in target[x:z] need to exist in triplets[i] at the equivalent index
        2. For each matching value in triplets[i] there must also be a value in a seperate triplet[j] <= triplets[i] - so that we can use max to get this number

        We need to check for the target value to exist in triplets and for any value <= target to merge with

        Use an array of 6 positions to store 6 booleans, first 3 store if we have found the value in target, last 3 store if we have found a value <= to use to merge
        '''

        found_a = False
        found_b = False
        found_c = False

        for triplet in triplets:

            if triplet[0] > target[0] or triplet[1] > target[1] or triplet[2] > target[2]:
                continue

            if triplet[0] == target[0]:
                found_a = True
            if triplet[1] == target[1]:
                found_b = True
            if triplet[2] == target[2]:
                found_c = True

            if found_a and found_b and found_c:
                return True
        
        return False 


        
        
