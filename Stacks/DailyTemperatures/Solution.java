import java.util.Stack;


class Solution {
    public int[] dailyTemperatures(int[] T) {
        int[] res = new int[T.length];
        Stack<Integer> stack = new Stack<Integer>();

        for (int i = 0; i < T.length; ++i) {
            while (!stack.isEmpty() && T[i] > T[stack.peek()]) {
                int index = stack.pop();
                res[index] = i - index;
            }
            stack.push(i);
        }

        return res;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        int[] T = {73,74,75,71,69,72,76,73};
        int[] res = s.dailyTemperatures(T);
        for (int num : res) {
            System.out.println(num);
        }
        
    }
}

//   0 1  2  3  4  5  6  7
/// 73,74,75,71,69,72,76,73
//                     ^            ^
//  
// stack: [2,5]
// index:  3
// res[index] = i - index = 5 - 2 = 2