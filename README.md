### Hash

### Stack

### Backtrack

### Notes
```
character space (1-26) is constant space
String s -> s.toCharArray() || s.charAt(index)
memo.put(c, memo.getOrDefault(c, 0) + 1);
memo.put('c') instead of memo.put("(");
Map<Character, Character> memo = new HashMap<Character, Character>();
java.util.EmptyStackException
use stack to store index or tuple maybe better when input list is fixed
int[] func(new int[]{1,2,3,4}) {}
return new Pair(1,2);
Scanner sc = new Scanner(System.in); int n = sc.nextInt();
List is an interface, cannot use func(new List<Integer>{}), use func(new ArrayList<Integer>{}) instead; 
dfs avoid infinity, when pass list by reference, need to create new arraylist return val, or it would be empty
error: List<Integer> res = new List<Integer>(), 
correct: List<String> res = new ArrayList<String>(), List is interface
Arrays.sort();
convert Set<List<Integer>> res = new HashSet<List<>>() to ArrayList<List<Integer>>(res);

```