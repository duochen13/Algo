/*
Given a non-empty array of integers, return the k most frequent elements.
Assumption: K is always valid

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]

1. construct heap with tuples in the format of (freq, num)
[(3,1), (2,2), (1,3)]
2. pop until N = K
*/


import java.util.PriorityQueue;
import java.util.HashMap;
import java.util.Map;
import java.util.Comparator;
import java.util.List;
import java.util.ArrayList;



class Pair<T, P> {
    T first;
    P second;
    Pair(T first, P second) { this.first = first; this.second= second; }
    public T getKey() { return this.first; }
    public P getValue() { return this.second; }
}

class NumComparator implements Comparator<Pair<Integer, Integer>> {
    public int compare(Pair<Integer, Integer> a, Pair<Integer, Integer> b) {
        return b.getKey() - a.getKey();
    }
}


class Solution {

    public List<Integer> topKFrequent(int[] nums, int k) {
        if (nums == null || nums.length == 0) {
            return new ArrayList<Integer>();
        }
        Map<Integer, Integer> memo = new HashMap<>();
        for (int num : nums) {
            memo.put(num, memo.getOrDefault(num, 0) + 1);
        }
        // Construct Max Heap
        PriorityQueue<Pair<Integer, Integer>> pq = new PriorityQueue<>(new NumComparator());
        for (int num : memo.keySet()) {
            pq.add(new Pair<Integer, Integer>(memo.get(num), num)); //(freq, num)
        }
        
        int i = 0;
        ArrayList<Integer> res = new ArrayList<Integer>();
        while (i < k) {
            Pair<Integer, Integer> cur = pq.poll();
            int num = cur.getValue();
            res.add(num);
            ++i;
        }
        return res;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        int[] nums = new int[]{1,1,2,2,2,2,2,4,4,4};
        int k = 2;
        List<Integer> res = s.topKFrequent(nums, k);
        for (int num : res) {
            System.out.print(num + " ");
        }

    }
}