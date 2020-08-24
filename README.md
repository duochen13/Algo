
### Hash
- [Two Sum 1](./Hash/TwoSum/Solution.java)

### Stack
- [ValidParentheses 20](./Stack/ValidParentheses/Solution.java)
- [TrappingRainWater 42](./Stack/TrappingRainWater/Solution.java)
- [LargestRectInHistogram 84](./Stack/LargestRectInHistogram/Solution.java)
```
42 & 84, care about condition of pushing to stack
```
- [DailyTemperature 739](./Stack/DailyTemperatures/Solution.java)
- [RemoveDuplicateLetters(TBD) 316](./Stack/RemoveDuplicateLetters/Solution.java)

### Tree
- [BalancedBinaryTree 110](./Tree/BalancedBinaryTree)
```
Classic recursion, top-down (intutive) vs bot-up (optimized, avoid double traversal)
```

### DFS
- [BinaryTreePath 257](./Tree/BinaryTreePath)
```
Tree recursion, or iteration (store tuple in stack)
```

### BFS
- [BinaryTreeRightSideView 199](./BFS/BinaryTreeRightSideView/Solution.java)
```
Level order BFS (iteration)
```

### Backtracking
- [CombinationSum 39 40 216](./Array/CombinationSum/Solution.java)




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
int -> Stirng: Integer.toString(2);
new Pair<TreeNode, String>, getValue(), getKey()
Deque<Integer> dq = new LinkedList<Integer>(), [add get peek poll][First Last]
List cancatenation, list.addAll(list.subList(start, end));
```

### TBR
```
Database: index in relational / non-relational database, how to handle concurrency, frequency of read and write
Denormalization(left): fewer joins, but hard to update
Courses            Teachers       |  Courses   Teachers
cid *tid (tname)   tid tname      |  cid *tid   tid tname
```

### BGM
- [Unravel](https://www.youtube.com/watch?v=xFMPBPOy9SI)
- [Sik-K](https://www.youtube.com/watch?v=36HvpOE4opQ)
- [Guren no Yumiya](https://www.youtube.com/watch?v=MIUQGbA8B4k)
- [Never Grow Up](https://www.youtube.com/watch?v=qw7oS1FBHyI)
- [Ignite](https://www.youtube.com/watch?v=sCwB3qKS_SQ)
- [Angel](https://www.youtube.com/watch?v=fOUfYU2NEJU)
- [Sanbonezakura](https://www.youtube.com/watch?v=LxkEr-3GCGU)
- [Loser](https://www.youtube.com/watch?v=Dx_fKPBPYUI)
- [Honey](https://www.youtube.com/watch?v=l3n6DiaELcc)
- [Way back home](https://www.youtube.com/watch?v=4KSDFEI5I00)
- [Lemon](https://www.youtube.com/watch?v=Gz1ldpRfg74)
- [Brave Heart](https://www.youtube.com/watch?v=YsTGTwqNfsQ)
- [Light of the Seven](https://www.youtube.com/watch?v=OCqMDeD6Fmc)
