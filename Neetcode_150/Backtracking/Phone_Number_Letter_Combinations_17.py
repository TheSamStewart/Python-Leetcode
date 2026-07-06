class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        '''
        hash table to store number and array with corresponding letters 
        '''

        if not digits:

            return []

        res = []

        phone_board = {
            1: [],                2: ['a', 'b','c'],    3: ['d','e','f'],
            4: ['g','h','i'],     5: ['j','k','l'],     6: ['m','n','o'],
            7: ['p','q','r','s'], 8: ['t','u','v'],     9: ['w','x','y','z']
        }

        def combinations(i, current_combination):

            if len(current_combination) == len(digits):

                res.append(current_combination[:])

                return

            for letter in phone_board[int(digits[i])]:

                combinations(i + 1, current_combination + letter)

        combinations(0 , "")

        return res
