import java.util.*;


class Solution {
    public List<int[]> twoSum(int[] nums, int target) {
        // List<List<Integer>> res = new ArrayList<List<Integer>>();
        List<int[]> res = new ArrayList<int[]>();

        Map<Integer, Integer> memo = new HashMap<>();
        
        for (int i = 0; i < nums.length; ++i) {
            int tmp = target - nums[i];
            if (memo.containsKey(tmp)) {
                int[] tmp_res = {i, memo.get(tmp)};
                res.add(tmp_res);
            } else {
                memo.put(nums[i], i);
            }
        }

        return res;
    }

    public List<int[]> twoSumSort(int[] nums, int target) {
        List<int[]> res = new ArrayList<int[]>();
        int l = 0, r = nums.length - 1;
        while (l < r) {
            int tmpSum = nums[l] + nums[r];
            if (tmpSum == target) {
                int[] tmpPair = {l, r};
                res.add(tmpPair);
                l += 1;
                r -= 1;
            } else if (tmpSum < target) {
                l += 1;
            } else {
                r -= 1;
            }
        }
        return res;
    }

    public static void main(String[] args) {
        int[] nums = {1,2,4,3,5,6};
        int target = 6;
        Solution s = new Solution();
        // List<int[]> r = s.twoSum(nums, target);
        List<int[]> r = s.twoSumSort(nums, target);
        for (int[] num_list : r) {
            for (int num : num_list) {
                System.out.print(num);
            }
            System.out.print('\n');
        }
    }
}