import java.util.*;


class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] res = new int[2];
        Map<Integer, Integer> memo = new HashMap<>();
        
        for (int i = 0; i < nums.length; ++i) {
            memo.put(nums[i], i);
        } for (int i = 0; i < nums.length; ++i) {
            int tmp = target - nums[i];
            if (memo.containsKey(tmp) && memo.get(tmp) != i) {
                res[0] = i;
                res[1] = memo.get(tmp);
                return res;
            }
        }

        return res;
    }

    public static void main(String[] args) {
        int[] nums = {1,3,5,6};
        int target = 6;
        Solution s = new Solution();
        int[] r = s.twoSum(nums, target);
        System.out.println(r[0]);
        System.out.println(r[1]);
    }
}