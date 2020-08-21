import java.util.Map;
import java.util.HashMap;
import java.util.Stack;

class Solution {

    public boolean isValid(String s) {
        
        Map<Character, Character> memo = new HashMap<Character, Character>();
        memo.put('(', ')');
        memo.put('{', '}');
        memo.put('[', ']');
        Stack<Character> stack = new Stack<>();

        for (char x : s.toCharArray()) {
            if (memo.containsKey(x)) {
                stack.push(x);
            } else {
                if (stack.isEmpty() || memo.get(stack.peek()) != x) {
                    return false;
                } else {
                    stack.pop();
                }
            }
        }

        return stack.isEmpty();
    }
    public static void main(String[] args) {
        Solution s = new Solution();
        boolean res = s.isValid("({})");
        System.out.println(res);
    }
}



// create a hashtable: {}
// traverse the characters
// if left braces: puhs to stack
// else: check if the current char match with the top element of the stack