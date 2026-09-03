class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        '''
        We are asked to find whether it is possible to visit each station once 

        Greedy solution - if current_gas - cost[i] < 0 - the starting index for the position must live after this point in the array
        '''

        if sum(cost) > sum(gas):
            return -1

        start = 0
        curr_gas = 0

        #iterate through each station

        for i in range(len(gas)):

            #add the gas[i] to curr_gas

            curr_gas += gas[i]

            #check for invalid travel route if curr_gas - cost[i] < 0:
            
            if curr_gas - cost[i] < 0:
                
                #we need to move our start pointer and reset gas
                start = i+1 
                curr_gas = 0

            else:

                curr_gas -= cost[i]

            #return start

        return start


        
