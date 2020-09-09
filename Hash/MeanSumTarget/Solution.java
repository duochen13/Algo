import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Map;
import java.util.HashMap;


class Solution {

    // brute force: construct a presum array
    public ArrayList<int[]> targetSumEqualsToBruteForce(int[] nums, int target) {
        ArrayList<int[]> res = new ArrayList<int[]>();
        int[] preSum = new int[nums.length + 1];

        for (int i = 0; i < nums.length; ++i) {
            preSum[i + 1] = preSum[i] + nums[i];
            // System.out.println("i: " + i + ", preSum[i + 1]: " + preSum[i + 1]);
        }
        for (int j = 0; j < preSum.length; ++j) {
            for (int i = 0; i < j; ++i) {
                int diff = preSum[j] - preSum[i], N = j - i;
                // System.out.println("diff: " + diff + ", N: " + N);
                if (diff == N * target) {
                    res.add(Arrays.copyOfRange(nums, i, j));
                }
            }
        }

        return res;
    }

    // HashTable: preSum[j] - preSum[i] = (j - 1) * target
    public ArrayList<int[]> targetSumEqualsTo(int[] nums, int target) {
        ArrayList<int[]> res = new ArrayList<int[]>();
        int[] preSum = new int[nums.length + 1];
        for (int i = 0; i < nums.length; ++i) {
            preSum[i + 1] = preSum[i] + nums[i];
            // System.out.println("i: " + i + ", preSum[i + 1]: " + preSum[i + 1]);
        }   
        Map<Integer, Integer> memo = new HashMap<>();
        for (int i = 0; i < preSum.length; ++i) {
            int tmp = preSum[i] - i * target;
            if (!memo.containsKey(tmp)) {
                memo.put(tmp, i);
            } else if (memo.containsKey(tmp) && i != memo.get(tmp)) {
                res.add(Arrays.copyOfRange(nums, memo.get(tmp), i));
            }
        }

        return res;
    }

    public static void main(String[] args) {
        int[] nums = new int[]{1,2,1,4,2};
        int target = 3;
        List<int[]> res = new Solution().targetSumEqualsTo(nums, target);
        for (int i = 0; i < res.size(); ++i) {
            for (int j = 0; j < res.get(i).length; ++j) {
                System.out.print(res.get(i)[j] + " ");
            }
            System.out.println();
        }
    }
}

/*
Given A = [2, 1, 3] and S = 2, output = 3, 
since the arithmetic means of fragments [2], [1, 3] and [2, 1, 3] are equal to 2.
Given A = [0, 4, 3, −1] and S = 2, your function should return 2, since fragments [0, 4] and [4, 3, −1] have an arithmetic mean equal to 2.

Given A = [2, 1, 4] and S = 3, your function should return 0, since there exist no contiguous fragments whose arithmetic mean is equal to 3.

*/