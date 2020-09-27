

import java.util.PriorityQueue;
import java.util.Comparator;
import java.util.Arrays;

class MeetingComparator implements Comparator<int[]> {
    public int compare(int[] a, int[] b) {
        return a[0] - b[0];
    }
}

class Solution {


    public int minMeetingRooms(int[][] intervals) {
        if (intervals == null || intervals.length == 0) {
            return 0;
        }
        Arrays.sort(intervals, new MeetingComparator());
        
        PriorityQueue<Integer> pq = new PriorityQueue<Integer>();
        pq.add(intervals[0][1]);
        
        for (int i = 1; i < intervals.length; ++i) {
            int curStart = intervals[i][0], curEnd = intervals[i][1];
            if (curStart >= pq.peek()) {
                pq.poll();
            }
            pq.add(curEnd);
        }
        return pq.size();
    }

    public static void main(String[] args) {

        int[][] intervals = new int[3][2];
        intervals[0] = new int[]{0,20};
        intervals[1] = new int[]{5,15};
        intervals[2] = new int[]{15,30};

        int res = new Solution().minMeetingRooms(intervals);
        System.out.println(res);
    }
}