
import java.util.Queue;
import java.util.LinkedList;

class Solution {
    public boolean canAttendMeetings(Integer[] intervals) {
        if (intervals.length == 0) {
            return true;
        }
        Arrays.sort(intervals);
        Queue<Pair<Integer, Integer>> q = new LinkedList<Pair>(Arrays.asList(intervals));
        while (!q.isEmpty()) {
            Pair<Integer, Integer> tmp = q.poll();
        }

        return false;
    }
}