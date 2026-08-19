import java.util.*;

class Solution {

    private String str;
    private int n;
    private Map<Integer, Integer> completed;


public int numDecodings(String s) {

    this.n = s.length();
    this.completed = new HashMap<>();
    this.str = s;

    return ways(0);
}

public int ways(int i){

    //If we have reached the end of the string this is a valid string and we can return this as 1 way

    if (i == n){
        return 1;
    }
        
    //Any single char selection that is zero/starts with zero is invalid so return 0

    if (str.charAt(i) == '0'){

        return 0;
    }

    //Check for completed work

    if (completed.containsKey(i)){

        return completed.get(i);

    }

    //Always choose one char path as this always has possibility of being valid

    int count = ways(i+1);

    //Check that i+2 is in bounds and that the value is valid 2 digit int

    if(i+1 < n){
        int twoDigit = Integer.parseInt(str.substring(i, i+2));
        if(twoDigit >= 10 && twoDigit <= 26){
            count += ways(i+2);
        }
    }

    //Add finished work to hasmap and return the count.

    completed.put(i, count);
    return count;            
    
}

}

        //How can we remeber work? 
