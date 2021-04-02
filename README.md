 ### HashTable
- [Group Anagram 49](./Hash/GroupAnagram)
```
sorted(bca) -> abc || keys = [0,1,0....0], len(keys) = 26
```
- [Ads Converation Rate](./Hash/AdsConversionRate/Solution.py)
- [TargetSum](./Hash/MeanSumTarget)

### LinkedList
- [Reverse Linked List 206](./LinkedList/ReverseLinkedList)
- [Clone LinkedList with Random Pointer 138](./LinkedList/CloneLinkedListWithRandPtr/Solution.py)
- [FlattenBinaryTreetoLinkedList 114](./Tree/FlattenBTtoLinkedList/Solution.java)

### Array
- [Partition Labels 763](./Array/PartitionLabels)
- [Missing Number](./Array/MissingNumber)
- [ContinuousSubarraySum](./Array/ContinuousSubarraySum/Solution.py)
```
two pointer
```
- [FindMissingNumberFromArithmeticSequence TBR](./Array/MissingNumber/Solution.py)

### Heap
- [Meeting Room 254](./Heap/MeetingRooms)
```
Arrays.sort(intervals, new Comparator<int[]>(){ public int compare(){}})
```
- [Top K Frequent Elements 347](./Heap/TopKFrequent)
- [Merge K LinkedList 23](./Heap/MergeKLinkedList)
```
Input can be a streaming of data (access with get() method) instead of a list, or divide & conquer
```
- [Median from Data Stream 295](./OOD/MedianFromDataStream/Solution.py)


### Stack
- [ValidParentheses 20](./Stack/ValidParentheses/Solution.java)
```
921, 1514 minimum inserts to make valid (), stack or one pass sol
```
- [TrappingRainWater 42](./Stack/TrappingRainWater/Solution.java)
- [LargestRectInHistogram 84](./Stack/LargestRectInHistogram/Solution.java)
```
42 & 84, care about condition of pushing to stack
```
- [DailyTemperature 739](./Stack/DailyTemperatures/Solution.java)
- [RemoveDuplicateLetters(TBD) 316](./Stack/RemoveDuplicateLetters/Solution.java)

### Tree
- [BalancedBinaryTree 110](./Tree/BalancedBinaryTree)
- [BoundaryOfBinaryTree 545](./Tree/BoundaryofBinaryTree/Solution.py)
- [FlattenBTtoLinkedList 114](./Tree/FlattenBTtoLinkedList)
- [FindCommonAncestorOfBinaryTree 235 236](./Tree/FindCommonAncestorOfBinaryTree)
```
BST -> BT -> N-ary Tree
```

### DFS
- [DividedToGroups](./DFS/DividedToGroups)
- [Number of Distinct Islands 694](./DFS/EqualMatrix)
- [Maximal Square 221](./DFS/MaximalSquare/Solution.py)
```
694-221
```
- [Pacific Atlantic Waterflow](./DFS/OceanWaterFlow)
- [GraphValidTree](./DFS/GraphValidTree)
- [MinimumHeightTree](./DFS/MinimumHeightTree)
```
TLE, tree dp + purning TBF, undirected graph
```
- [Course Schedule 207](./DFS/CourseSchedule)
- [Path from Source to Dest 1059](./DFS/PathFromSourceToDest)
```
DAG, states: {unvisted, visiting, visited}
```
- [Reconstruct Itinerary 322](./DFS/ReconstructItinerary)
```
DAG
```
- [Find Leaves of Binary Tree 366](./DFS/FindLeavesOfBinaryTree)
- [All Paths from Source to Target 797](./DFS/AllPathsFromSourceToTarget/Solution.py)
- [Number of Island, Largest Path](./DFS/FindLargestIntPath/Solution.cpp)

### BFS
- [BinaryTreeRightSideView 199](./BFS/BinaryTreeRightSideView/Solution.java)
- [WordLadder](./BFS/WordLadder/Solution.java)
- [Shortest Distance from All Buildings](./BFS/ShortestDistanceFromBuildings/Solution.py)
- [Shortest Path with Obstacle Elimination](./BFS/ShortestPathObstaclesElimination/Solution.py)
- [Amazon Locker](./BFS/AmazonLocker/Solution.py)
- [Alien Dictionary](./BFS/AlienDictionary)
```
BFS in DAG, Toposort, course schedule emmm
```

### Backtracking
- [CombinationSum 39 40 216](./DFS/CombinationSum/Solution.py)
```
sorted or not, res[:] or res
```

### DP
- [RodCutting](./DP/RodCutting/Solution.py)
- [CoinChange](./DP/coinChange/Solution.py)
- [LongestPalindromicSubstring](./DP/longestPalindromicSubstr)
- [LongestContinuousCommonSubArray](./DP/longestCommonSubArray)
```
dp[i,j]: LCCA of A[:i] and B[:j],  dp[i,j] = dp[i + 1][j + 1] + 1 if A[i] == B[j]
```
- [LongestIncreasingSubsequence 300](./DP/longestIncreasingSubsequence)
```
dp[i,j]: LISS of nums[i:j], dp[j] = max(dp[j], dp[i] + 1) if nums[i] < nums[j]
```
- [LongestCommonSubsequence 1143](./DP/longestCommonSubsequence)

- [LongestStringChain 1048](./DP/longestStringChain)

- [WordBreak 139 140](./DP/wordBreak/Solution.py)
```
dp[i]: s[:i] is workbreakable, dp[j] = dp[i]   if A[i:j] in wordDict, 140 TLE
```

- [Edit Distance 72](./DP/editDistance/Solution.py)
```
dp[i,j]: number of operations from wordA[:i] to wordB[j:].  dp[i][j] = dp[i - 1][j - 1] if wordA[i] == wordB[j], dp[i][j] = 1 + max(insert, delete, swap)  
```
- [Matrix Chain Manipulation](./DP/MatrixChainMultiplication/Solution.py)


### Algorithms
- [Fisher-Yates Shuffle](./Algos/Fisher-Yates/Solution.py)
```
If it's how random.shuffle() implemented
```
- [Floyd's Cycle Detection](./Algos/FloydCycleDetection/Solution.py)
- [Garbage Collection in Java](./Algos/GarbageCollection/Solution.java)
- [QuickSort](./Algos/QuickSort/Solution.py)
- [KMP TBR](./Algos/KMP/Solution.java)
- [BinarySearch](./Algos/BinarySearch)
- [MergeSort](./Algos/MergeSort)
- [CountSort](./Algos/CountSort)
- [FuzzySort](./Algos/FuzzySort)

### Divide & Conquer
- [Closest points](./DivideAndConquer/ClosestPoints/Solution.py)

### Bit Manipulation
- [Power of 4](./BitManipulation/PowerOfFour/Solution.py)

### OOD
- [Queen's Gambit'](./OOD/QueensGambit/Solution.py)
- [LRU Cache](./OOD/LRUCache/Solution.java)
- [Random Number Generator](./Algos/Fisher-Yates)
- [Median from Data Stream 295](./OOD/MedianFromDataStream)
- [Top K Frequent from Data Stream](./OOD/TopKDataStream/Solution.py)
- [ParkingLot](./OOD/ParkingLot/Solution.java)
- [Java Interface & Abstract class](./OOD/JavaOOD/Solution.java)
- [Templates](./OOD/Templates/play.cpp)
- [Functor](./OOD/Functor/test.cpp)

### System Design
- [Tiny URL](./SystemDesign/TinyURL)

### Security
- [Devil Pointer](./HackSpice)

### Vim 
Key Bindings | Pattern
```
Jump based on relativenumber | <number><direction>
Visual mode: 5j(jump down 5 lines), 3i(jump up 3 lines), very helpful when enable 'set relativenumber', (no ruler plz)

Execute program within editor | <shift> + ':' + '!' + <command>
Sometimes I need to :wq and run some program and go back to editor, but !<command> helps run program within vim. If <command> is empty, :! will simply run last command

Comment / Uncomment multiple lines
<control> + v: enter visual mode, <esc> + v may not work, it will select blocks of lines instead of first column in the next step
Select the lines that you want to comment / uncomment
Comment: <shift> + i: Enter the insertion mode, type the comment sign: #, // etc. Then <ESC>
Uncomment: d

Navigate between file structure and file content
vim . in current directory
:NERDTree
<control> + w(double click) to navigate between windows 
```

Userful Plugins:
```
gmarik/Vundle.vim: Best package manager for lazy people(maybe?)
preservim/nerdtree: File structure and menu bar
Valloric/YouCompleteMe: Finally works in macos 10.14 
zxqfl/tabnine-vim: Neural Network + YouCompleteMe, but slows vim down
morhetz/gruvbox: Best color scheme for py i guess? not suitable for cpp though
```



### BGM
- [Marasy Playlist](https://www.youtube.com/watch?v=AHv0vP6jQvg)
- [You Lie in April](https://www.youtube.com/watch?v=nQ8uAWxhlU0)
- [Shining/Snow-Rain](https://www.youtube.com/watch?v=dBem3WfTnXc)
- [Lemon](https://www.youtube.com/watch?v=spfLnDJPDF4)
- [からくりピエロ](https://www.youtube.com/watch?v=l82y3WIaqW0&list=RDMMl82y3WIaqW0&start_radio=1)
- [Karakuri Pierrot](https://www.youtube.com/watch?v=l82y3WIaqW0)
- [BigYear](https://www.youtube.com/watch?v=qJoAHZKqSDY)
- [Unravel](https://www.youtube.com/watch?v=xFMPBPOy9SI)
- [Sik-K](https://www.youtube.com/watch?v=36HvpOE4opQ)
- [Guren no Yumiya](https://www.youtube.com/watch?v=MIUQGbA8B4k)
- [Never Grow Up](https://www.youtube.com/watch?v=qw7oS1FBHyI)
- [YOASOBI](https://www.youtube.com/watch?v=EQ1McdUbglg)
- [Goose House (Uncle A)](https://www.youtube.com/watch?v=zsVAbS8xmaU)
- [Ignite](https://www.youtube.com/watch?v=sCwB3qKS_SQ)
- [Angel](https://www.youtube.com/watch?v=fOUfYU2NEJU)
- [Sanbonezakura](https://www.youtube.com/watch?v=LxkEr-3GCGU)
- [Loser](https://www.youtube.com/watch?v=Dx_fKPBPYUI)
- [Honey](https://www.youtube.com/watch?v=l3n6DiaELcc)
- [Way back home](https://www.youtube.com/watch?v=4KSDFEI5I00)
- [Lemon](https://www.youtube.com/watch?v=Gz1ldpRfg74)
- [Brave Heart](https://www.youtube.com/watch?v=YsTGTwqNfsQ)
- [Light of the Seven](https://www.youtube.com/watch?v=OCqMDeD6Fmc)
- [Anime OP Combo](https://www.youtube.com/watch?v=Obfw2O6vNXE)
- [AOA OP Combo](https://www.youtube.com/watch?v=gyk54CsyFoA)

