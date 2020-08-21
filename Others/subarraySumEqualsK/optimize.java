import java.util.Map;
import java.util.HashMap;

public class optimize {
    public static int subarraySum(int[] nums, int k) {
        int res = 0, tmp = 0;
        Map<Integer, Integer> memo = new HashMap<>();
        memo.put(0, 1);
        for (int i = 0; i < nums.length; ++i) {
            tmp += nums[i];
            if (memo.containsKey(tmp - k))
                res += memo.get(tmp - k);
            memp[tmp] = memo.getDefault(tmp, 0) + 1; 
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
