/*
1. dp(i): length of increasing subarray in A[:i]

2. dp(0) = 0

3. for A[i:j], if A[i] < A[j]:
   dp[i] = max(dp[i], dp[j] + 1)


ex:       0  1   2  3   4   5   6   7   8
 i   j   10  22  9  33  21  50  41  60  80
[..] 1    0   1 [10]
     2    0   1  0
     3    0   1  0   2 [10, 22]
     4    0   1  0   2  1
     5    0   1  0   2  1   3 [10, 22, 33]
     6    0   1  0   2  1   3   3
     7    0   1  0   2  1   3   3   4 [10, 22, 33, 50]
     8    0   1  0   2  1   3   3   4   5 [10, 22, 33, 50, 60]

res: [10,22,33,50,60,80] 
*/

import java.util.ArrayList;
import java.util.List;


class Solution {

public List<Integer> longestIncreasingSubsequence(int[] nums) {
    int[] dp = new int[nums.length];
    ArrayList<Integer>[] memo = new ArrayList[nums.length];
    for (int i = 0; i < nums.length; ++i) {
        if (memo[i] == null) {
            memo[i] = new ArrayList<Integer>();
        }
        memo[i].add(nums[i]);
    }


    for (int j = 0; j < nums.length; ++j) {
        int k = 0;
        for (int i = 0; i < j; ++i) {
            if (nums[i] < nums[j]) {
                if (dp[i] + 1 > dp[j]) {
                    dp[j] = dp[i] + 1;
                    k = i;
                }
            }
        }
        ArrayList<Integer> tmp = memo[k];
        tmp.add(nums[j]);
        memo[j] = tmp;
    }

    return memo[nums.length - 1];
}



    public static void main(String[] args) {
        // System.out.println(new Solution().longestIncreasingSubsequence(new int[]{10,22,9,33,21,50,41,60,80}));
    }
}