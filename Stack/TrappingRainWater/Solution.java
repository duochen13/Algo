import java.util.Stack;


class Solution {

    public int trap(int[] height) {

        Stack<Integer> stack = new Stack<Integer>();

        int i = 0, res = 0;
        while (i < height.length) {
            // may trap water
            if (stack.isEmpty() || height[i] <= height[stack.peek()]) {
                stack.push(i);
                i += 1;
            } else {
                // lowerest
                int top = stack.pop();
                if (stack.isEmpty()) {
                    continue;
                }
                // min(left_border, right_boder) * (x diff)
                res += (Math.min(height[stack.peek()], height[i]) - height[top]) * (i - stack.peek() - 1);
            }
        }

        return res;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        int[] height = {0,1,0,2,1,0,1,3,2,1,2,1};
        int res = s.trap(height);
        System.out.println(res);
    }
}