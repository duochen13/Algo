
// Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

// Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?


// Input: numCourses = 2, prerequisites = [[1,0]]
// Output: true
// Explanation: There are a total of 2 courses to take. 
//     To take course 1 you should have finished course 0. So it is possible.

// 6
// [[0,1],[1,2],[3,4]]
// output: true

// 0: []
// 1: [0]      
// 2: [1]   
// 3: []]
// 4: [3]
// visited: [0, 1, 2, 3, 4]

// [[0,1],[1,2],[2,1]]
// 0: []
// 1: [0, 2]
// 2: [1]
// visited: [0 1 2]
//           1 0 0


import java.util.Map;
import java.util.HashMap;
import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;

// Before starting
// are edges duplicated?
// convert adjacncy metrices 

// General idea
// starting from 1 node doing dfs, use a list to check if there exist a cycle

// Analysis:
// O(n), O(n)

class Solution {

    public boolean dfs(int start, HashMap<Integer, ArrayList<Integer>> memo, int[] visited, ArrayList<Integer> res) {

        if (visited[start] == 1){
            return false;
        } else if (visited[start] == 2) {
            return true;
        }
        // visiting
        visited[start] = 1;

        if (memo.containsKey(i)) {
            for (int j : memo.get(start)) {
                if (!dfs(j, memo, visited, res)) {
                    return false;
                }
            }
        }

        // visited
        visited[start] = 2;

        res.add(start);

        return true;
    }

    public int[] canFinish(int numCourses, int[][] prerequisites) {

        if (prerequisites == null) return new int[]{};

        int[] visited = new int[numCourses];
        // unvisited
        Arrays.fill(visited, 0, numCourses, 0);
        HashMap<Integer, ArrayList<Integer>> memo = new HashMap<Integer, ArrayList<Integer>>();

        for (int[] tmp : prerequisites) {
            if (memo.containsKey(tmp[1])) {
                memo.get(tmp[1]).add(tmp[0]);
            } else {
                ArrayList<Integer> arr = new ArrayList<Integer>();
                arr.add(tmp[0]);
                memo.put(tmp[1], arr);
            }
        }

        ArrayList<Integer> res = new ArrayList<Integer>();
 
        for (int i = 0; i < numCourses; ++i) {
            if (!dfs(i, memo, visited, res)) {
                return new int[]{};
            }
        }

        return res.toArray();
    }
}
