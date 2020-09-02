public class Solution {
    public boolean isValid(String str) {
        Stack<Character> stack = new Stack<>();

        Map<Character, Character> memo = new HashMap<>();
        memo.put(')', '(');
        memo.put(']', '[');
        memo.put('{', '}');

        for (int i = 0; i < str.length(); ++i) {
            char s = str.charAt(i);
            // left brace
            if (!memo.containsKey(s))
                stack.push(s);
                // right brace
            else {
                if (stack.isEmpty() || memo.get(s) != stack.pop())
                    return false;
            }
            System.out.println(stack.peek());

        }//for

        return stack.isEmpty() ? true : false;
    }

    public static void main(String[] args) {
        System.out.println("hello world");
    }
}