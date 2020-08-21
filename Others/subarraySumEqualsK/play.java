public class play {
    public static int subarraySum(int[] nums, int k) {
        int res = 0;
        int[] pre_sum = new int[nums.length + 1];
        for (int i = 0; i < nums.length; ++i) {
            // System.out.println(pre_sum[i]);
            pre_sum[i + 1] = pre_sum[i] + nums[i];
        }
        for (int i = 0; i < pre_sum.length; ++i) {
            for (int j = 0; j < i; ++j) {
                if (pre_sum[i] - pre_sum[j] == k)
                    res += 1;
            }
        }
        return res;
    }


    public static void main(String[] args) {
        int[] nums = new int[]{1,1,1};
        int k = 2;
        int res = subarraySum(nums, k);
        System.out.println(res);
    }


}
