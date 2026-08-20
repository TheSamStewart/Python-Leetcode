import java.util.*;

class Solution {

    private int[] coins;
    private Map<Integer, Integer> completed;

    public int coinChange(int[] coins, int amount) {

        
        this.coins = coins;
        this.completed = new HashMap<Integer, Integer>();

        //return -1 if no valid solution else return min coins
        int result = helper(amount);
        return result == Integer.MAX_VALUE ? -1 : result;
        
    }
    public int helper(int remaining){

        //If remaining is below zero, this is an invalid combination
        //Return inf as to not edit min coins
         if(remaining < 0){
            return Integer.MAX_VALUE;
        }
        
        //Check for completed work
        if (completed.containsKey(remaining)){
            return completed.get(remaining);
        } 
        
        //This means we have a valid solution and need to start the return up the call stack
        if(remaining == 0){
            return 0;
        }

        int min_coins = Integer.MAX_VALUE;

        //Iterate through coins and call the function, this tests all combinations
        for(int c : coins){

            int res = helper(remaining-c);

            //To prevent overflow
            if(res != Integer.MAX_VALUE){
                min_coins = Math.min(min_coins, res+1);
            }
            
        }

        completed.put(remaining, min_coins);
        return min_coins;

    }
}
