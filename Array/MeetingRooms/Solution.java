
import java.util.Queue;
import java.util.LinkedList;
import java.util.Arrays;
import java.util.PriorityQueue;


class Solution {
    public boolean canAttendMeetings(int[][] intervals) {
        if (intervals.length == 0) {
            return true;
        }
        Arrays.sort(intervals);
        int preStart = intervals[0][0];
        int preEnd = intervals[0][1];
        for (int i = 1; i < intervals.length; ++i) {
            int curStart = intervals[i][0];
            int curEnd = intervals[i][1];
            if (curStart < preEnd)
                return false;
            preStart = curStart;
            preEnd = curEnd;
        }
        return true;
    }

    public int Meetings(int[][] intervals) {
        Arrays.sort(intervals, (a, b) -> a[0] - b[0]);
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        int cnt = 0;

        for (int[] interval : intervals) {
            if (pq.isEmpty()) {
                cnt += 1;
                pq.offer(interval[1]);
            } else {
                if (interval[0] >= pq.peek()) {
                    pq.poll();
                } else {
                    cnt += 1;
                }
                pq.offer(interval[1]);
            }
        }
        return cnt;
    }

    public static void main(String[] args) {
        int[][] intervals = new int[4][2];
        intervals[0] = new int[]{0, 20};
        intervals[1] = new int[]{5, 15};
        intervals[2] = new int[]{15, 30};
        intervals[3] = new int[]{30 ,40};

        Solution s = new Solution();
        int res = s.Meetings(intervals);
        System.out.println(res);
    }
}
