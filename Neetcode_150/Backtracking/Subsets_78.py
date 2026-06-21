class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = [[]]


        for num in nums:

            new_subs = []

            for curr in res:


                #+ here ignores the empty (null) set
                new_subset = curr + [num]
                new_subs.append(new_subset)

            #adds to the array cleanly
            res.extend(new_subs)

        return res
        