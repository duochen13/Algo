
### HashTable
- [Group Anagram 49](./Hash/GroupAnagram/Solution.java)
```
sorted(bca) -> abc || keys = [0,1,0....0], len(keys) = 26
```
- [Ads Converation Rate](./Hash/AdsConversionRate/Solution.py)
- [TargetSum](./Hash/MeanSumTarget/Solution.java)

### LinkedList
- [Reverse Linked List 206](./LinkedList/ReverseLinkedList/Solution.java)
- [FlattenBinaryTreetoLinkedList 114](./Tree/FlattenBTtoLinkedList/Solution.java)

### Array
- [Meeting Room 254](./Stack/MeetingRooms/Solution.java)
```
heap solution is not optimal
```

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
- [FlattenBTtoLinkedList 114](./Tree/FlattenBTtoLinkedList)
- [FindCommonAncestorOfBinaryTree 235](./Tree/FindCommonAncestorOfBinaryTree)
```
TBR iterative solution
```

### DFS
- [BinaryTreePath 257](./Tree/BinaryTreePath)
```
Tree recursion, or iteration (store tuple in stack)
```
- [Course Schedule 207](./DFS/CourseSchedule)
```
omg DAG question
```
- [Number of Island, Largest Path](./DF/FindLargestIntPath)


### BFS
- [BinaryTreeRightSideView 199](./BFS/BinaryTreeRightSideView/Solution.java)
```
Level order BFS (iteration)
```

### Backtracking
- [CombinationSum 39 40 216](./Array/CombinationSum/Solution.java)
```
sorted or not, res[:] or res
```

### DP
- [LongestContinuousCommonSubArray](./DP/longestCommonSubArray)
```
dp[i,j]: LCCA of A[:i] and B[:j],  dp[i,j] = dp[i + 1][j + 1] + 1 if A[i] == B[j]
```
- [LongestIncreasingSubsequence 300](./DP/longestIncreasingSubsequence)
```
dp[i,j]: LISS of nums[i:j], dp[j] = max(dp[j], dp[i] + 1) if nums[i] < nums[j]
```

- [WordBreak 139 140](./DP/wordBreak/Solution.py)
```
dp[i]: s[:i] is workbreakable, dp[j] = dp[i]   if A[i:j] in wordDict, 140 TLE
```

### Algorithms
- [KMP TBR](./Algos/KMP/Solution.java)
- [QuickSort](./Algos/QuickSort/Solution.java)

### OOD
- [Borrow and return books at library TBR](./OOD/library/Library.java)

### Notes
```
Scanner sc = new Scanner(System.in); int n = sc.nextInt();
ArrayList<T>() -> T[]: arrayList.toArray();
String s -> s.toCharArray() || s.charAt(index)
memo.put(c, memo.getOrDefault(c, 0) + 1);
memo.put('c') instead of memo.put("(");
counter[x - 'a]++;
hm.forEach((k, v) -> System.out.println(k + ": " + (v + 10)));
return new Array(memo.values());  memo.values(): collections list
return new Pair(1,2);
dfs avoid infinity, when pass list by reference, need to create new one
arraylist return val, or it would be empty
Arrays.sort(nums, (a,b) -> (a - b));
new LinkedList<>(Arrays.asList(arr));
convert Set<List<Integer>> res = new HashSet<List<>>() to ArrayList<List<Integer>>(res);
Integer -> Stirng: Integer.toString(2);
String -Integer: Integer.parseInt(cnt)
new Pair<TreeNode, String>, getValue(), getKey()
Deque<Integer> dq = new LinkedList<Integer>(), [add get peek poll][First Last]
PriorityQueue<Integer> pq = new PriorityQueue<>(); offer, poll, add
List cancatenation, list.addAll(list.subList(start, end));
String.indexOf("prefix");
hashMap.keySet()
aString.split("\\."), "." means any character in regular expression
```

### TBR
```
Database: index in relational / non-relational database, how to handle concurrency, frequency of read and write
Denormalization(left): fewer joins, but hard to update
Courses            Teachers       |  Courses   Teachers
cid *tid (tname)   tid tname      |  cid *tid   tid tname
HashMap (not thread-safe), HashTable(thread-safe, disallow null key-value pair) ConcurrentHashMap(thread-safe, but lock every HashEntry instead of the whole key value pairs), 只锁被不同thread touch的entry，如果不同thread对不同的entry进行操作
Heap (store objs, new String()), Stack (store programs)
Unsigned ints (hold a large positive value, no negative value), signed (hold both postive and negative numbers)
Arrays.copyOfRange(nums, i, j)
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
