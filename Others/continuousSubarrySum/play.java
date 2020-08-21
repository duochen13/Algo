public class play {
    public static boolean checkSubarraySum(int[] nums, int k) {
        int[] pre_sum = new int[nums.length + 1];
        for (int i = 0; i < nums.length; ++i) {
            pre_sum[i + 1] = pre_sum[i] + nums[i];
        }
        for (int i = 0; i < pre_sum.length; ++i) {
            for (int j = 0; j < i; ++j) {
                int diff = pre_sum[i] - pre_sum[j];
                if ((diff == k || (k != 0 && (diff % k == 0))) && i > j) {
                    return true;
                }
            }
        }
        print_helper(pre_sum);    
        return false;
    }

    public static void print_helper(int[] nums) {
        for (int i = 0; i < nums.length; ++i) {
            System.out.println(nums[i]);
        }
    }

    public static void main(String[] args) {
        int[] nums = new int[]{23, 2, 4, 6, 7};
        int k = 7;
        boolean res = checkSubarraySum(nums, k);
        System.out.println("res: " + res);
    }
}
