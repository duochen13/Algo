class Solution {
    public int largestRectangleArea(int[] heights) {
        int res = 0, i = 0;
        Stack<Integer> stack = new Stack<>();
        while (i < heights.length) {
            if (stack.isEmpty() || heights[i] >= heights[stack.peek()]) {
                stack.push(i);
                i += 1;
            } else {
                int tmpIndex = stack.peek();
                stack.pop();
                int area = heights[tmpIndex] * (i - tmpIndex);
                res = Math.max(res, area);
            }
        }
        // elements in stack is in increasing order
        while (!stack.isEmpty()) {
            int tmpIndex = stack.peek();
            stack.pop();
            int area = heights[tmpIndex] * (i - tmpIndex);
            res = Math.max(res, area);
        }
        
        return res;
    }
}

// 0 1 2 3 4 5
// 2 1 5 6 2 3

// 
// s = [0, 1]
// res: 1