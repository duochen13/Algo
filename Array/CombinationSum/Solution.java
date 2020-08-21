import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;


class Solution {

    public Set<List<Integer>> tmp = new HashSet<List<Integer>>();

    public void dfs(int start, int[] candidates, int target, List<Integer> currents, Set<List<Integer>> res) {

        if (target == 0) {
            // res.add(currents);
            res.add(new ArrayList<Integer>(currents));
            return;
        } else if (target < 0) {
            return;
        }
        for (int i = start; i < candidates.length; ++i) {
            currents.add(candidates[i]);
            dfs(i + 1, candidates, target - candidates[i], currents, res);
            currents.remove(currents.size() - 1);
        }
    }

    public List<List<Integer>> combSumEnableDuplicates(int[] candidates, int target) {
        List<Integer> currents = new ArrayList<Integer>();
        // List<List<Integer>> res = new ArrayList<List<Integer>>();
        Set<List<Integer>> res = new HashSet<List<Integer>>();
        Arrays.sort(candidates);
        dfs(0, candidates, target, currents, res);
        return new ArrayList<List<Integer>>(res);
    }


    public static void main(String[] args) {
        Solution s = new Solution();
        List<List<Integer>> res = s.combSumEnableDuplicates(new int[]{10,1,2,7,6,1,5}, 8);

        for (int i = 0; i < res.size(); ++i) {
            List<Integer> list = res.get(i);
            for (int j = 0; j < list.size(); ++j) {
                System.out.print(list.get(j));
                System.out.print(" ");
            }
            System.out.println();
        }
    }
}


// Q: how to avoid duplicated result?
// A: 

// candidates: [2 3 6 7]
// target: 7
// [7], [2,2,3]

// dfs(target, tmp):
    //   if target == 0:
    //     return tmp
    //   for num in candidates:
    //     dfs(target - num, tmp + [num])