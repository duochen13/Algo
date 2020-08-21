
// Description
// Imagine that an employment tree represents the formal employee hierarchy at Amazon. Manager nodes have
// chid nodes for each employee that reports to them; each of these employees can, in turn, have child nodes
// representing their respective reportees. Each node in the tree contains an integer representing the number of
// months the employee has spent at the company. Team tenure is computed as the average tenure of the manager
// and all the company employees working below the manager. The oldest team has the highest team tenure.
// Write an algorithm to find the manager of the team with the highest tenure. An employee must have child nodes
// to be a manager.

// Input
// The input to the function/method consists of an argument -
// president, a node representing the root node of the employee hierarchy.

// Output
// Return the node which has the oldest team.

// Note
// There will be at least one child node in the tree and there will be no ties.

// Ref: https://leetcode.com/discuss/interview-question/797541/amazon-online-assessment-2-sde-1-new-graduate-2021-coding-2-questions-with-solutions

import java.util.*;

class Pair{
	int totalNodes, totalSum;
	Pair(int total, int sum){
		this.totalNodes = total;
		this.totalSum = sum;
	}
}

class Solution {
    public static Pair findHighestTenure(HashMap<Integer, ArrayList<Integer>> hmap, int V){

        return new Pair(1,1);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
        HashMap<Integer, ArrayList<Integer>> hmap = new HashMap<> ();
        
        for (int i = 0; i < n; ++i) {
            int parent = sc.nextInt();
            int child = sc.nextInt();
            if (hmap.containsKey(parent)) {
                hmap.get(parent).add(child);
            } else {
                ArrayList<Integer> tmp = new ArrayList<>();
                tmp.add(child);
                hmap.put(parent, tmp);
            }
        }
        int parentNode = sc.nextInt();

    }

}